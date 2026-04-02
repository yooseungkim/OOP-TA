# 📚 GIST Autograder System

A Python & Streamlit-based **autograding tool** for programming assignments in **C/C++**. Designed for **GIST** courses (e.g., `GS1401`, `GS2408`) to manage testcases, compile/run student submissions, and export results interactively via Web GUI.

---

## 🛠️ How to Run

- Python 3.7+
- `streamlit`
- `pandas`
- C/C++ Compiler (`g++` or `gcc`)

```bash
# 필수 파이썬 패키지 설치
pip install streamlit pandas
```

## 🌟 Key Features

- ✅ **Web-based GUI:** Streamlit을 활용한 직관적인 대화형 인터페이스.
- ✅ **Advanced Evaluation Metrics:** - `numeric`: 출력 텍스트 안에서 숫자(소수점/음수 포함)만 추출해 정답 부분 수열(Subsequence) 일치 여부 확인.
  - `contains`: 정답의 단어들이 학생 출력에 순서대로 포함되어 있는지 확인.
  - `exact`, `any` 등 다양한 채점 방식 지원.
- ✅ **Rubric-based Penalty System:** - `Major Mistake`: 정답 불일치 또는 런타임 에러 시 **-4점**.
  - `Constraint`: 필수 키워드/함수명 누락 또는 금지어 사용 시 **-2점**.
  - `Late`: 파일명에 `LATE` 포함 시 **-2점**.
- ✅ **Session-Specific Testcases:** 분반(Session)별로 문제가 다를 경우, 특정 분반(예: `lab1_1`) 전용 테스트케이스 적용 가능.
- ✅ **Multi-file Compilation:** 메인 코드 외에 `Car.cpp`, `Student.cpp` 등 다중 소스 파일 동시 컴파일 지원.
- ✅ **Lab Score Summary:** 개별 Exercise 채점 결과들을 묶어 Lab 전체의 종합 점수(Total Points) CSV로 자동 병합.
