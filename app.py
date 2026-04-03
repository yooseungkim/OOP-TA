import glob
import os
import re
import subprocess

import pandas as pd
import streamlit as st

# --- Custom CSS for Larger Tabs ---
st.set_page_config(page_title="GIST Autograder", layout="wide")
st.markdown(
    """
    <style>
    /* 탭 크기 및 폰트 확대 */
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        padding: 0.5rem 1rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def is_subsequence(expected_list, output_list):
    if not expected_list:
        return False
    it = iter(output_list)
    return all(exp in it for exp in expected_list)


def normalize_whitespace(text):
    return " ".join(text.split())


def evaluate_output(output, expected, method):
    out_norm = normalize_whitespace(output)
    exp_norm = normalize_whitespace(expected)

    if method == 'exact':
        return out_norm == exp_norm
    elif method == 'any':
        return True
    elif method == 'numeric':
        out_nums = re.findall(r'-?\d+\.?\d*', output)
        exp_nums = re.findall(r'-?\d+\.?\d*', expected)
        return is_subsequence(exp_nums, out_nums)
    elif method == 'contains':
        out_words = out_norm.split()
        exp_words = exp_norm.split()
        return is_subsequence(exp_words, out_words)
    return False


def check_keywords(source_code, req_keys, forb_keys):
    req_list = [k.strip() for k in req_keys.split(',')
                ] if req_keys.strip() else []
    forb_list = [k.strip() for k in forb_keys.split(',')
                 ] if forb_keys.strip() else []

    missing_req = [k for k in req_list if not re.search(
        rf'\b{re.escape(k)}\b', source_code)]
    used_forb = [k for k in forb_list if re.search(
        rf'\b{re.escape(k)}\b', source_code)]

    return missing_req, used_forb


def grade_exercise(lab, ex, points, method, compiler, std, recompile, base_dir, req_keys, forb_keys, add_files):
    submission_dir = os.path.join(base_dir, f"Submission/Lab{lab}")
    tc_dir = os.path.join(submission_dir, "Testcase")
    answer_dir = os.path.join(submission_dir, "Answer")

    if not os.path.exists(submission_dir):
        st.error(f"Directory not found: {submission_dir}")
        return pd.DataFrame()

    ext = ".cpp" if compiler == "g++" else ".c"
    ans_source = os.path.join(answer_dir, f"ex{lab}_{ex}{ext}")
    ans_bin = os.path.join(answer_dir, f"ex{lab}_{ex}")
    has_ans_source = os.path.isfile(ans_source)

    ans_add_files_str = " ".join(
        [os.path.join(answer_dir, f) for f in add_files]) if add_files else ""

    if has_ans_source:
        try:
            subprocess.run(
                f"{compiler} -std={std} {ans_source} {ans_add_files_str} -o {ans_bin}", shell=True, check=True)
        except subprocess.CalledProcessError:
            st.error("Answer source compile error. (추가 파일이 Answer 폴더에도 있는지 확인하세요)")
            return pd.DataFrame()

    scores = []
    sessions = [d for d in os.listdir(submission_dir) if os.path.isdir(
        os.path.join(submission_dir, d)) and d not in ["Answer", "Testcase"]]

    for session in sessions:
        session_dir = os.path.join(submission_dir, session)
        students = [d for d in os.listdir(
            session_dir) if os.path.isdir(os.path.join(session_dir, d))]

        for student_id in students:
            student_path = os.path.join(session_dir, student_id)
            search_pattern = os.path.join(student_path, f"*ex{lab}_{ex}*{ext}")
            source_files = glob.glob(search_pattern)

            result_row = {"Session #": session, "Student ID": student_id}

            if not source_files:
                result_row[f"Points{ex}"] = 0
                result_row["Status"] = "No Submission"
                result_row["Combined_Output"] = ""
                scores.append(result_row)
                continue

            source_file = source_files[0]
            is_late = "LATE" in os.path.basename(source_file).upper()
            compile_path = os.path.join(student_path, f"ex{lab}_{ex}_bin")

            combined_outputs = []
            penalties = []
            earned_points = points

            with open(source_file, 'r', encoding='utf-8', errors='ignore') as f:
                source_code = f.read()

            missing_req, used_forb = check_keywords(
                source_code, req_keys, forb_keys)
            if missing_req or used_forb:
                penalties.append("Constraint(-2)")
                earned_points -= 2
                err_msgs = []
                if missing_req:
                    err_msgs.append(f"Missing: {', '.join(missing_req)}")
                if used_forb:
                    err_msgs.append(f"Forbidden: {', '.join(used_forb)}")
                combined_outputs.append(
                    f"[Keyword Violation] {' | '.join(err_msgs)}")

            stud_add_files_str = " ".join(
                [os.path.join(student_path, f) for f in add_files]) if add_files else ""

            if recompile or not os.path.isfile(compile_path):
                compile_cmd = f"{compiler} -std={std} {source_file} {stud_add_files_str} -o {compile_path}"
                compile_process = subprocess.run(
                    compile_cmd, shell=True, capture_output=True, text=True)
                if compile_process.returncode != 0:
                    result_row[f"Points{ex}"] = 0
                    result_row["Status"] = "Compile Error"
                    result_row["Combined_Output"] = compile_process.stderr.strip()
                    scores.append(result_row)
                    continue

            all_correct = True
            tc_index = 1
            runtime_error_flag = False

            while True:
                session_tc_path = os.path.join(
                    tc_dir, f"{session}_ex{lab}_{ex}_{tc_index}.txt")
                default_tc_path = os.path.join(
                    tc_dir, f"ex{lab}_{ex}_{tc_index}.txt")
                tc_path = session_tc_path if os.path.exists(
                    session_tc_path) else default_tc_path

                if not os.path.exists(tc_path):
                    break

                with open(tc_path, 'r') as f:
                    tc_input = f.read()

                if has_ans_source:
                    ans_output = subprocess.run(
                        [ans_bin], input=tc_input, capture_output=True, text=True).stdout
                else:
                    ans_out_path = os.path.join(
                        answer_dir, f"ex{lab}_{ex}_{tc_index}.txt")
                    ans_output = open(ans_out_path, 'r').read(
                    ) if os.path.exists(ans_out_path) else ""

                try:
                    student_exec = subprocess.run(
                        [compile_path], input=tc_input, capture_output=True, text=True, timeout=5)
                    if student_exec.returncode != 0:
                        result_row[f"TC{ex}_{tc_index}"] = "Runtime Error"
                        current_output = f"TC{tc_index} STDERR:\n{student_exec.stderr.strip()}"
                        all_correct = False
                        runtime_error_flag = True
                    else:
                        is_correct = evaluate_output(
                            student_exec.stdout, ans_output, method)
                        result_row[f"TC{ex}_{tc_index}"] = "O" if is_correct else "X"
                        current_output = student_exec.stdout.strip()
                        if not is_correct:
                            all_correct = False
                except subprocess.TimeoutExpired:
                    result_row[f"TC{ex}_{tc_index}"] = "Time Out"
                    current_output = f"TC{tc_index} STDERR: 무한 루프 또는 시간 초과 (5초)"
                    all_correct = False
                    runtime_error_flag = True

                result_row[f"Output{ex}_{tc_index}"] = current_output
                combined_outputs.append(f"[TC{tc_index}] {current_output}")
                tc_index += 1

            if is_late:
                penalties.append("Late(-2)")
                earned_points -= 2

            if not all_correct or runtime_error_flag:
                penalties.append("Major Mistake(-4)")
                earned_points -= 4

            earned_points = max(0, earned_points)

            if not penalties:
                result_row["Status"] = "OK"
            else:
                result_row["Status"] = ", ".join(penalties)

            result_row[f"Points{ex}"] = earned_points
            result_row["Combined_Output"] = " | ".join(combined_outputs)
            scores.append(result_row)

    return pd.DataFrame(scores)


def summarize_scores(lab, base_dir):
    score_dir = os.path.join(base_dir, f"Scores/Lab{lab}")
    if not os.path.isdir(score_dir):
        return pd.DataFrame(), f"❌ Lab {lab}에 대한 점수 폴더({score_dir})를 찾을 수 없습니다."

    csv_files = glob.glob(os.path.join(score_dir, f"ex{lab}_*_score.csv"))
    if not csv_files:
        return pd.DataFrame(), f"❌ Lab {lab} 폴더 안에 채점된 CSV 파일이 없습니다."

    summary_df = pd.DataFrame(columns=['Session #', 'Student ID'])

    for file in csv_files:
        try:
            df = pd.read_csv(file)
            point_col = [col for col in df.columns if col.startswith('Points')]

            if point_col:
                ex_num = point_col[0].replace('Points', '')
                status_col_name = f'Status{ex_num}'
                cols_to_keep = ['Session #', 'Student ID', point_col[0]]

                if 'Status' in df.columns:
                    df = df.rename(columns={'Status': status_col_name})
                    cols_to_keep.append(status_col_name)

                summary_df = pd.merge(summary_df, df[cols_to_keep], on=[
                                      'Session #', 'Student ID'], how='outer')
        except Exception as e:
            return pd.DataFrame(), f"❌ 파일({file})을 읽는 중 에러 발생: {str(e)}"

    point_cols = [
        col for col in summary_df.columns if col.startswith('Points')]
    status_cols = [
        col for col in summary_df.columns if col.startswith('Status')]

    summary_df[point_cols] = summary_df[point_cols].apply(
        pd.to_numeric, errors='coerce').fillna(0)
    summary_df['Total Points'] = summary_df[point_cols].sum(axis=1)

    for col in status_cols:
        summary_df[col] = summary_df[col].fillna("-")

    ex_nums = sorted([int(col.replace('Points', '')) for col in point_cols])
    ordered_cols = ['Session #', 'Student ID', 'Total Points']

    for num in ex_nums:
        ordered_cols.append(f'Points{num}')
        if f'Status{num}' in summary_df.columns:
            ordered_cols.append(f'Status{num}')

    summary_df = summary_df[ordered_cols]
    summary_df = summary_df.sort_values(
        by=['Session #', 'Student ID']).reset_index(drop=True)

    return summary_df, "success"


# --- UI Setup ---
st.title("📚 GIST Autograder System")

# 탭 4개 유지 (수동 실행기 포함)
tab_grade, tab_tc, tab_summary, tab_runner = st.tabs(
    ["Grader", "Testcase Manager", "Lab Score Summary", "Manual Runner"])

with tab_grade:
    with st.sidebar:
        st.header("📁 Directory Settings")
        base_dir = st.text_input(
            "Base Directory Path", value=os.getcwd(), help="상위 폴더의 절대 경로를 입력하세요.")

        if os.path.exists(os.path.join(base_dir, "Submission")):
            st.success("✅ Submission 폴더가 감지되었습니다.")
        else:
            st.error("❌ 경로 내에 Submission 폴더가 없습니다.")

        st.divider()
        st.header("⚙️ Grading & Compiler Options")

        col1, col2 = st.columns(2)
        with col1:
            lab_num = st.number_input("Lab Num", min_value=1, value=1, step=1)
            points = st.number_input("Points", min_value=1, value=5, step=1)
            compiler = st.selectbox("Compiler", ["g++", "gcc"])

        with col2:
            ex_num = st.number_input("Ex Num", min_value=1, value=1, step=1)
            method = st.selectbox(
                "Evaluation Method",
                ["numeric", "contains", "exact", "any"],
                help="""
            **채점 방식(Evaluation Metric) 안내**
            - **numeric**: 정답의 모든 숫자가 학생 출력 내에 '부분 수열'로 순서대로 존재하면 정답입니다. (중간에 다른 숫자가 끼어 있어도 정답 처리)
            - **contains**: 정답의 모든 단어가 학생 출력 내에 '부분 수열'로 순서대로 등장하면 정답입니다. (중간에 다른 단어가 출력되어도 정답 처리)
            - **exact**: 학생의 출력값과 정답이 완벽히 일치해야 정답입니다.
            - **any**: 에러 없이 정상 종료되기만 하면 정답입니다.
            - **주의**: numeric과 contains는 부정확할 수 있으므로 결과를 직접 확인하시길 바랍니다. 
            """
            )
            std = st.text_input(
                "-std", value="c++11" if compiler == "g++" else "c11")

        additional_files_str = st.text_input(
            "Additional Files (Optional)",
            value="",
            help="메인 소스 코드 외에 함께 컴파일해야 할 파일이 있다면 확장자를 포함하여 쉼표(,)로 구분해 입력하세요. (예: Car.cpp, Student.cpp)"
        )

        add_files = [f.strip() for f in additional_files_str.split(
            ',')] if additional_files_str.strip() else []

        for file_name in add_files:
            if compiler == "g++" and file_name.endswith(".c"):
                st.error(f"⚠️ 경고: 컴파일러가 g++인데 C 파일({file_name})이 포함되어 있습니다.")
            elif compiler == "gcc" and (file_name.endswith(".cpp") or file_name.endswith(".cc")):
                st.error(f"⚠️ 경고: 컴파일러가 gcc인데 C++ 파일({file_name})이 포함되어 있습니다.")

        recompile = st.checkbox(
            "Force Recompile",
            value=False,
            help="체크 시 이전에 만들어둔 실행 파일(bin)을 무시하고 무조건 다시 컴파일합니다."
        )

        st.divider()
        st.subheader("📜 Source Code Rules")
        req_keys = st.text_input(
            "Required Keywords (CSV)",
            value="",
            help="e.g., for, while. (지시된 Function name 강제도 이곳에 기재하세요). 미준수 시 -2점"
        )
        forb_keys = st.text_input(
            "Forbidden Keywords (CSV)",
            value="",
            help="e.g., goto. (사용이 금지된 Function name 등). 미준수 시 -2점"
        )

        st.write("")
        run_btn = st.button("Run Grader 🚀", type="primary",
                            use_container_width=True)

    if run_btn:
        with st.spinner('Compiling and Grading in progress...'):
            df = grade_exercise(lab_num, ex_num, points, method, compiler,
                                std, recompile, base_dir, req_keys, forb_keys, add_files)
            st.session_state['graded_df'] = df
            st.session_state['current_lab'] = lab_num
            st.session_state['current_ex'] = ex_num

    if 'graded_df' in st.session_state and not st.session_state['graded_df'].empty:
        df = st.session_state['graded_df']
        c_lab = st.session_state['current_lab']
        c_ex = st.session_state['current_ex']

        st.success("🎉 Grading Completed!")

        cols = df.columns.tolist()
        if "Status" in cols:
            cols.insert(2, cols.pop(cols.index("Status")))
            df = df[cols]

        st.dataframe(df, use_container_width=True)

        os.makedirs(os.path.join(
            base_dir, f"Scores/Lab{c_lab}"), exist_ok=True)
        csv_path = os.path.join(
            base_dir, f"Scores/Lab{c_lab}/ex{c_lab}_{c_ex}_score.csv")
        df.to_csv(csv_path, index=False)

        col_down1, col_down2 = st.columns([1, 4])
        with col_down1:
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Results as CSV",
                data=csv,
                file_name=f'Lab{c_lab}_ex{c_ex}_score.csv',
                mime='text/csv',
            )
        with col_down2:
            st.info(f"💡 다운로드하지 않아도 **{csv_path}** 경로에 이미 자동 저장되어 있습니다.")

        st.divider()
        if st.button("초기 화면으로 돌아가기"):
            del st.session_state['graded_df']
            st.rerun()

    else:
        st.markdown("### 🌟 Welcome to GIST Autograder System")
        st.markdown(
            "이 프로그램은 C/C++ 프로그래밍 과제를 자동으로 컴파일하고 채점해 주는 웹 기반 툴입니다.\n좌측 사이드바에서 디렉토리 경로와 옵션을 설정한 후 **Run Grader 🚀** 버튼을 클릭하세요.")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            #### 💡 점수 기준 
            * **GS1401:** Pre-practice: 5pts, In-practice 10pts             
            * **GS2408:** 일괄 5pts
            * **Late (-2점):** 지각 제출 시 (파일명 `LATE` 감지)
            * **Constraint (-2점):** 지정된 필수 키워드/함수명 누락 또는 금지 키워드 사용
            * **Compile Error / No Submission:** 0점 처리
                        
            #### 성적 확인 
            * Lab Summary에서 종합할 Lab 선택 후 확인 
            * Minor/Major mistake 학생의 경우, Manual Runner 탭에서 간편 실행 후 출력 확인 가능
            """)

        with col2:
            st.markdown("""
            #### 📁 파일 구조 안내 (Directory Structure)
            ```text
            Base_Directory/
            ├── 📂 Submission/          
            │   └── Lab1/            
            │       ├── Answer/      <- 정답코드 또는 테스트케이스 정답
            │       ├── Testcase/    <- 테스트케이스 입력 파일
            │       ├── lab1_1/      <- 분반 (Session)
            │       └── lab1_2/      
            └── 📂 Scores/              
            ```
            """)

with tab_tc:
    st.header("📝 Testcase Manager")
    col1, col2, col3 = st.columns(3)

    with col1:
        tc_lab = st.number_input(
            "Lab Number", min_value=1, value=1, step=1, key="lab_t")
    with col2:
        tc_ex = st.number_input(
            "Exercise Number", min_value=1, value=1, step=1, key="ex_t")
    with col3:
        tc_no = st.number_input(
            "Testcase Number", min_value=1, value=1, step=1, key="tc_t")

    st.markdown("### Session Prefix (분반 지정)")
    st.caption("분반마다 문제가 달라서 **특정 분반 전용 테스트케이스**를 만들어야 할 때 사용합니다. (예: `lab1_1` 학생들만 다른 문제를 풀 경우). **모든 분반이 동일한 문제라면 비워두시면 됩니다.**")
    session_prefix = st.text_input(
        "**분반 폴더명** 입력 (Optional, e.g. `lab1_1`, `lab3_2`)", value="", help="입력된 이름이 파일명 맨 앞에 추가되어 분반 전용 파일로 인식됩니다.")

    prefix = f"{session_prefix.strip()}_" if session_prefix.strip() else ""
    expected_file_name = f"{prefix}ex{tc_lab}_{tc_ex}_{tc_no}.txt"
    st.info(f"👀 **생성될 파일 이름 (Preview):** `{expected_file_name}`")
    st.markdown("---")

    tc_input_text = st.text_area("Testcase Input (STDIN)", height=150)
    tc_answer_text = st.text_area(
        "Expected Output (STDOUT - Optional if using answer.cpp)", height=150)

    if st.button("Save Testcase 💾"):
        base_dir = st.session_state.get('base_dir', os.getcwd())
        tc_target_dir = os.path.join(
            base_dir, f"Submission/Lab{tc_lab}/Testcase")
        ans_target_dir = os.path.join(
            base_dir, f"Submission/Lab{tc_lab}/Answer")

        os.makedirs(tc_target_dir, exist_ok=True)
        os.makedirs(ans_target_dir, exist_ok=True)

        tc_file_path = os.path.join(tc_target_dir, expected_file_name)
        ans_file_path = os.path.join(ans_target_dir, expected_file_name)

        with open(tc_file_path, "w") as f:
            f.write(tc_input_text)

        with open(ans_file_path, "w") as f:
            f.write(tc_answer_text)

        st.success(
            f"Testcase saved successfully to:\n- `{tc_file_path}`\n- `{ans_file_path}`")

with tab_summary:
    st.header("📊 Lab Score Summary")
    st.markdown(
        "개별 Exercise 점수가 채점된 CSV 파일들을 하나의 Lab 단위 종합 점수표로 병합합니다. (감점 사유 포함)")

    sum_lab_num = st.number_input(
        "Summarize Lab Number", min_value=1, value=1, step=1, key="lab_s")

    if st.button("Generate Summary 📈", type="primary"):
        base_dir = st.session_state.get('base_dir', os.getcwd())

        with st.spinner("Merging CSV files..."):
            summary_df, msg = summarize_scores(sum_lab_num, base_dir)

        if not summary_df.empty:
            st.success("성공적으로 점수와 감점 사유를 병합했습니다!")
            st.dataframe(summary_df, use_container_width=True)

            score_dir = os.path.join(base_dir, f"Scores/Lab{sum_lab_num}")
            os.makedirs(score_dir, exist_ok=True)
            summary_csv_path = os.path.join(
                score_dir, f"Lab{sum_lab_num}_Summary.csv")
            summary_df.to_csv(summary_csv_path, index=False)

            col_sum_down1, col_sum_down2 = st.columns([1, 4])
            with col_sum_down1:
                csv_data = summary_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download Summary CSV",
                    data=csv_data,
                    file_name=f'Lab{sum_lab_num}_Summary.csv',
                    mime='text/csv',
                )
            with col_sum_down2:
                st.info(
                    f"💡 다운로드하지 않아도 **{summary_csv_path}** 경로에 이미 자동 저장되어 있습니다.")
        else:
            st.warning(msg)

# --- 새로운 탭: Manual Code Runner ---
with tab_runner:
    st.header("🏃‍♂️ Manual Code Runner")
    st.markdown("오답이나 무한 루프가 의심되는 특정 학생의 코드를 직접 테스트케이스를 넣어보며 디버깅할 수 있습니다.")

    col_run1, col_run2, col_run3 = st.columns(3)
    with col_run1:
        run_lab = st.number_input(
            "Lab Number", min_value=1, value=1, step=1, key="run_l")
    with col_run2:
        run_ex = st.number_input(
            "Exercise Number", min_value=1, value=1, step=1, key="run_e")
    with col_run3:
        run_id = st.text_input("Student ID", placeholder="e.g., s20231234")

    st.markdown("---")
    col_run4, col_run5 = st.columns(2)
    with col_run4:
        run_compiler = st.selectbox(
            "Compiler Override", ["g++", "gcc"], key="run_c")
    with col_run5:
        run_std = st.text_input(
            "-std Override", value="c++11" if run_compiler == "g++" else "c11", key="run_std")

    run_input = st.text_area("Custom Stdin (Testcase Input)",
                             height=150, placeholder="여기에 입력할 테스트케이스 텍스트를 적어주세요.")

    if st.button("Run Student Code 🚀", type="primary"):
        base_dir = st.session_state.get('base_dir', os.getcwd())
        lab_dir = os.path.join(base_dir, f"Submission/Lab{run_lab}")

        if not run_id.strip():
            st.warning("학번(Student ID)을 입력해주세요.")
        elif not os.path.exists(lab_dir):
            st.error(f"❌ Lab 폴더를 찾을 수 없습니다: {lab_dir}")
        else:
            student_target_dir = None
            for session in os.listdir(lab_dir):
                potential_dir = os.path.join(lab_dir, session, run_id.strip())
                if os.path.isdir(potential_dir) and session not in ['Answer', 'Testcase']:
                    student_target_dir = potential_dir
                    break

            if not student_target_dir:
                st.error(
                    f"❌ '{run_id}' 학생의 제출 폴더를 찾을 수 없습니다. (Submission 폴더 내부를 확인해주세요)")
            else:
                ext = ".cpp" if run_compiler == "g++" else ".c"
                search_pattern = os.path.join(
                    student_target_dir, f"*ex{run_lab}_{run_ex}*{ext}")
                source_files = glob.glob(search_pattern)

                if not source_files:
                    st.error(
                        f"❌ 해당 학생의 ex{run_lab}_{run_ex} 소스코드 파일을 찾을 수 없습니다.")
                else:
                    source_file = source_files[0]
                    compile_path = os.path.join(
                        student_target_dir, f"ex{run_lab}_{run_ex}_manual_bin")

                    st.info(f"📄 **대상 파일:** `{source_file}`")

                    with st.spinner("Compiling code..."):
                        compile_cmd = f"{run_compiler} -std={run_std} {source_file} -o {compile_path}"
                        compile_process = subprocess.run(
                            compile_cmd, shell=True, capture_output=True, text=True)

                    if compile_process.returncode != 0:
                        st.error("💥 컴파일 에러 발생 (Compile Error)")
                        st.code(compile_process.stderr.strip(),
                                language="bash")
                    else:
                        st.success("✅ 컴파일 성공. 코드를 실행합니다.")
                        with st.spinner("Running code... (Max timeout: 5s)"):
                            try:
                                student_exec = subprocess.run(
                                    [compile_path],
                                    input=run_input,
                                    capture_output=True,
                                    text=True,
                                    timeout=5
                                )

                                col_out1, col_out2 = st.columns(2)
                                with col_out1:
                                    st.markdown(
                                        "### 🟢 Standard Output (stdout)")
                                    if student_exec.stdout.strip():
                                        st.code(
                                            student_exec.stdout.strip(), language="text")
                                    else:
                                        st.caption("출력 내용이 없습니다.")

                                    if student_exec.returncode != 0:
                                        st.error(
                                            f"⚠️ 프로그램이 비정상 종료되었습니다. (Return code: {student_exec.returncode})")

                                with col_out2:
                                    st.markdown(
                                        "### 🔴 Standard Error (stderr)")
                                    if student_exec.stderr.strip():
                                        st.code(
                                            student_exec.stderr.strip(), language="text")
                                    else:
                                        st.caption("에러 내용이 없습니다.")

                            except subprocess.TimeoutExpired:
                                st.error(
                                    "⏱️ **실행 시간 초과 (Timeout)!** 프로그램이 5초 넘게 응답하지 않습니다. (무한 루프나 무한 대기 상태가 의심됩니다)")
