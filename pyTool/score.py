import pandas as pd
import sys

scores = []
session_scores = []
student_score = []
columns = ["SESSION NO", "STUDENT ID"]

lab_no, ex_no = sys.argv[1], sys.argv[2]
TXT_PATH = f"../Scores/Lab{lab_no}/ex{lab_no}_{ex_no}_score.txt"
CSV_PATH = f"../Scores/Lab{lab_no}/ex{lab_no}_{ex_no}.csv"


def get_last(string: str, parse: str = "/") -> str:
    return string.split(parse)[-1]


with open(TXT_PATH, "r") as f:
    session = 1
    for line in f.readlines():
        line = line.strip()
        if line == "=====COMPLETE=====":
            break
        elif line == "=====NEXT SESSION=====":
            session += 1
            scores += session_scores
            session_scores = []
        elif line == "=====NEXT STUDENT=====":
            session_scores.append(student_score)
            student_score = []
        else:
            if not student_score:
                student_score = [session, get_last(line)]
            else:
                student_score.append(line)
testcases = (len(scores[0]) - 2) // 2
for i in range(testcases):
    columns += [f"TC{i + 1}", f"ANS{i + 1}"]
for i in range(len(scores)):
    df = pd.DataFrame(scores, columns=columns)
    df.to_csv(CSV_PATH, index=False)
