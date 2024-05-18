import pandas as pd
import openpyxl

scores = []
session_scores = []
student_score = []


def get_last(string: str, parse: str = "/") -> str:
    return string.split(parse)[-1]


with open("./score.txt", "r") as f:
    lab_no = int(f.readline())
    ex_no = int(f.readline())
    for line in f.readlines():
        line = line.strip()
        if line == "=====COMPLETE=====":
            break
        elif line == "=====NEXT SESSION=====":
            scores.append(session_scores)
            session_scores = []
        elif line == "=====NEXT STUDENT=====":
            session_scores.append(student_score)
            student_score = []
        else:
            if not student_score:
                student_score.append(get_last(line))
            else:
                student_score.append(line)

for i in range(len(scores)):
    df = pd.DataFrame(scores[i])
    df.to_csv("score.csv", index=False, header=False)
