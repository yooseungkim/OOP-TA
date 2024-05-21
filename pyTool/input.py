import sys

lab, ex, tc = map(int, sys.argv[1:])

answer_path = f"../Submission/Lab{lab}/Answer"
tc_path = f"../Submission/Lab{lab}/Testcase"

for i in range(1, tc + 1):
    testcase = open(f"{tc_path}/ex{lab}_{ex}_{i}.txt", "w")
    testcase.write(
        input("Enter Testcase(use \\n to make new line):").replace("\\n", "\n"))
    testcase.close()
    answer = open(f"{answer_path}/ex{lab}_{ex}_{i}.txt", "w")
    answer.write(
        input("Enter Answer(use \\n to make new line):").replace("\\n", "\n"))
    answer.close()
