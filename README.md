# 📚 GIST Autograder System

A Python-based **autograding tool** for programming assignments in **C/C++**, designed to manage testcases, compile and run student submissions, and export results to CSV.
Built for use in **GIST** courses including `GS1401` and `GS2408`.

## 요약

1. 파일 구조에 맞게 재배치 (Directory Structure 참고)
   1. cse 서버에서 학생 제출 파일 가지고오기
   2. Testcase 디렉토리에 txt파일 추가 또는 Grader 실행 후 Testcase Manager로 testcase 추가
   3. Answer 디렉토리에 **정답 소스코드 추가(권장)** 또는 2.와 같은 방법으로 추가
   4. 만약 소스코드로 사용한다면, Testcase Manager에서 answer을 건너 뛰어도됨
   5. 파일 이름이 맞지 않다면 제대로 작동하지 않으므로 참고하여 작성할 것.
2. Autograder 실행
   1. 채점 또는 관리하고자 하는 Lab 번호를 매개변수로 하여 프로그램 실행
      (Lab3를 채점하고자 하면,  `python main.py 3`)
3. Grader
   1. 저장된 Testcase와 Answer(txt 또는 .cpp)를 바탕으로 채점
   2. grader option으로 point, cpp, -std, method, files 지정 가능
      1. point: 현재 채점하는 Exercise의 배점 (기본: 10점)
      2. cpp: cpp 또는 c로 컴파일. (g++  / gcc)
      3. -std: language standard 설정 (몇몇 경우에 c++11, c++99 등으로 설정해주어야 오류가 나지 않는 경우가 있음)
      4. method: 'exact'- 일반적인 채점, 'any'-제출 후 실행만 되면 정답 (정해진 정답이 없는 경우)
      5. files: 추가 소스파일(main이 있는 파일 제외) (Cars.cpp, Circles.cpp 등 추가 파일)
   3. 가장 마지막에 출력되는 경로로 해당 Exercise의 채점 결과 저장
4. Lab Score Summary
   1. 한 Lab의 모든 Exercise를 채점했다면, 실행하여 종합 성적을 저장

---

## 📦 Features

- ✅ Testcase creation, preview, and modification
- ✅ Compile and grade C/C++ submissions
- ✅ Automatic comparison against answer files
- ✅ Export scores to CSV
- ✅ Summarize lab performance by session

---

## 🛠️ Dependencies

- Python 3.6+
- `pandas`
- C/C++ Compiler (`g++` or `gcc`)
- Unix-based environment (uses `rm`, `printf`, etc.)

---

## 📁 Directory Structure

```
.
├── main.py              # This autograder file
├── Submission/       # Contains Lab submission folders per session
│   └── Lab1/         # Lab#
│       ├── Answer/      # Stores answer files (exX_Y.cpp or exX_Y.txt) 
│       │   ├─ ex1_1.cpp # [Recommended, will update other answer files with corresponding testcase files 
│       │   ├─ ex1_1.txt
│       │   └─ ex1_2.txt
│       ├── Testcase/    # Stores testcase input files
│       │   ├─ ex1_1.txt
│       │   └─ ex1_2.txt
│       ├── Lab1/
│       │    └── student_id/
│       │    │   ├── ex1_1.cpp # Submission Source Code
│       │    │   ├── ex1_2.cpp
│       │    │   ├── ex1_3.cpp
│       │    │   └── ...
│       │    └── student_id/
│       │        └── ...
│       └── Lab2/
│           ├── student_id/
│           └── ...
├── Scores/           # Output CSV scores
│   └── Lab1/
│       ├── ex1_1.csv # Score for each exercise
│       ├── ex2_2.csv
│       ├── ... 
│       └── Lab1.csv  # Lab1 Summary
```

---

## 🚀 How to Use

### 1️⃣ Run the autograder

```bash
python main.py <lab_number>
```

Example:

```bash
python main.py 1
```

Optional kwargs:

```bash
python main.py 1 recompile=true padding=60 compiler=gcc
```

| Option        | Description                                |
| ------------- | ------------------------------------------ |
| `recompile` | Force recompilation (true/**false**) |
| `padding`   | Output padding (int)                       |
| `compiler`  | Compiler to use (`g++` or `gcc`)       |

For GS1401, use `compiler=gcc`. For GS2401, use default value(`compiler=g++`)

`recompile=True` will recompile for all submissions in any case Use when you are grading with other compiler option(`gcc/g++/c+11/c17...`) [Slower]

`recompile=False` will not recompile if corresponding **executable file exists.** If executable file not exists, it will compile the source code. [Faster/Default option]

---

### 2️⃣ Menu Options

After launching:

```
[1] Testcase Manager      → Create/modify/delete testcases
[2] EX Grader             → Compile & test student submissions
[3] Lab Score Summary  → Merge & summarize CSV scores
[4/0] Exit
```

---

### 3️⃣ Menu Options for Testcase Manager

After selecting `[1]Testcase`

```
[1] Preview     → Preview testcase input & output
[2] Add         → Add new testcase input & output
[3] Modify	→ Modify testcase input & output
[4] Delete	→ Delete Testcase 
[5/0] Exit	→ Exit without saving
```

---

### 4️⃣ Grading Submissions and Make Summary

First, grade for each exercise with `[2] Ex Grader`

You can set grading options, including points for this exercise (default 10), complier, language standard, recompilation.

After grading all exercises, make summary with `[3] Lab Score Summary`

### 🧪 Testcase Naming Format

| File Type | Format                          |
| --------- | ------------------------------- |
| Input     | `ex<lab>_<ex>_<tc>.txt`       |
| Answer    | `ex<lab>_<ex>_<tc>.cpp / txt` |

Example for Lab 1, Exercise 2, Testcase 3:

- Input: `ex1_2_3.txt` in `Testcase/`
- Answer: `ex1_2_3.txt` in `Answer/`

You can manually create testcases by adding new files in testcase and answer directories. In this case, make sure you follow the naming format and directory.

**Recommended to add source file (.cpp/.c) as an answer file instead of .txt.**

Grader will use this source file and its output for grading.

If you're using source file, answer txt file only exists for checking its output. (Not used for grading)

---

## 📤 Output

- Grading results exported to:`../Scores/Lab<lab>/ex<lab>_<ex>_score.csv`

| Session # | Student ID | TC3_1 | ANS3_1        | TC3_2 | ANS3_2        | TC3_3 | ANS3_3        | TC3_4 | ANS3_4        | Points3 |
| --------- | ---------- | ----- | ------------- | ----- | ------------- | ----- | ------------- | ----- | ------------- | ------- |
| Lab1      | s20215049  | X     | No Submission | X     | No Submission | X     | No Submission | X     | No Submission | 0       |
| Lab1      | s20215047  | O     | hello world   | O     | hello world   | O     | hello world   | O     | hello world   | 10      |
| Lab1      | s20215048  | X     | Hello, World  | X     | Hello, World  | X     | Hello, World  | X     | Hello, World  | 0       |
| Lab1      | s20215050  | X     | No Submission | X     | No Submission | X     | No Submission | X     | No Submission | 0       |
| Lab2      | s20215052  | X     | No Submission | X     | No Submission | X     | No Submission | X     | No Submission | 0       |
| Lab2      | s20215054  | X     | No Submission | X     | No Submission | X     | No Submission | X     | No Submission | 0       |
| Lab2      | s20215053  | X     | No Submission | X     | No Submission | X     | No Submission | X     | No Submission | 0       |

Lab summary exported to: `../Scores/Lab<lab>/Lab<lab>.csv`

| Session # | Student ID | Total Points | Points1 | Points2 | Points3 | Points4 |
| --------- | ---------- | ------------ | ------- | ------- | ------- | ------- |
| Lab1      | s20215047  | 10           | 0       | 0       | 10      | 0       |
| Lab1      | s20215048  | 0            | 0       | 0       | 0       | 0       |
| Lab1      | s20215049  | 0            | 0       | 0       | 0       | 0       |
| Lab1      | s20215050  | 0            | 0       | 0       | 0       | 0       |
| Lab2      | s20215051  | 0            | 0       | 0       | 0       | 0       |
| Lab2      | s20215052  | 0            | 0       | 0       | 0       | 0       |
| Lab2      | s20215053  | 0            | 0       | 0       | 0       | 0       |
| Lab2      | s20215054  | 0            | 0       | 0       | 0       | 0       |

---

## 🧑‍💻 Author

**Yooseung Kim**
[Contact: yooseungkim@gm.gist.ac.kr](mailto:yooseungkim@gm.gist.ac.kr)
Dept. of EECS, Gwangju Institute of Science and Technology
