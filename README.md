# 📚 GIST Autograder System

A Python-based **autograding tool** for programming assignments in **C/C++**, designed to manage testcases, compile and run student submissions, and export results to CSV.
Built for use in **GIST** courses including `GS1401` and `GS2408`.

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
│       ├── Answer/      # Stores answer files (exX_Y.txt) 
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

| Option        | Description                          |
| ------------- | ------------------------------------ |
| `recompile` | Force recompilation (true/false)     |
| `padding`   | Output padding (int)                 |
| `compiler`  | Compiler to use (`g++` or `gcc`) |

---

### 2️⃣ Menu Options

After launching:

```
[1] Testcase Manager      → Create/modify/delete testcases
[2] EX Grader             → Compile & test student submissions
[3] Lab Score Summarizer  → Merge & summarize CSV scores
[4/0] Exit
```

---

### 🧪 Testcase Naming Format

| File Type | Format                    |
| --------- | ------------------------- |
| Input     | `ex<lab>_<ex>_<tc>.txt` |
| Answer    | `ex<lab>_<ex>_<tc>.txt` |

Example for Lab 1, Exercise 2, Testcase 3:

- Input: `ex1_2_3.txt` in `Testcase/`
- Answer: `ex1_2_3.txt` in `Answer/`

---

## 📤 Output

- Grading results exported to:`../Scores/Lab<lab>/ex<lab>_<ex>_score.csv`
- Lab summary exported to:
  `../Scores/Lab<lab>/Lab<lab>.csv`

---

## 🖍 Terminal Colors

The script uses ANSI escape codes for color formatting (works in Unix-like terminals).
Colors include: `RED`, `GREEN`, `YELLOW`, `BLUE`, `CYAN`, etc.

---

## 🧑‍💻 Author

- **Yooseung Kim**
  Dept. of EECS, GIST
  [Email Me](mailto:yooseungkim@gm.gist.ac.kr)
