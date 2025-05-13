import pandas as pd
import sys
import os
import subprocess

BLACK = "\\e[0;30m"
RED = "\\e[0;31m"
GREEN = "\\e[0;32m"
YELLOW = "\\e[0;33m"
BLUE = "\\e[0;34m"
MAGENTA = "\\e[0;35m"
CYAN = "\\e[0;36m"
GRAY = "\\e[0;37m"
WHITE = "\\e[0;38m"


def printf(string: str, color: str = "", end: str = "\n") -> None:
    os.system(f'printf "{color}{string}{end}{WHITE}"')


def _copyright():
    printf(
        f"{RED}GIST {WHITE}Computer Programming Assignment Autograder [GS1401/GS2408]")
    printf("©Yooseung Kim, GIST EECS".rjust(60), BLUE)


class Testcase:
    def __init__(self, lab, ex, tc_no, tc="", answer=""):
        self.lab = lab
        self.ex = ex
        self.tc_no = tc_no
        self.new_tc_no = tc_no
        self.input = tc
        self.output = answer
        self.padding = 50
        self.is_new = False
        self.read_testcase()

    @property
    def answer_path(self):
        return f"../Submission/Lab{self.lab}/Answer/ex{self.lab}_{self.ex}_{self.tc_no}.txt"

    @property
    def tc_path(self):
        return f"../Submission/Lab{self.lab}/Testcase/ex{self.lab}_{self.ex}_{self.tc_no}.txt"

    @property
    def new_answer_path(self):
        return f"../Submission/Lab{self.lab}/Answer/ex{self.lab}_{self.ex}_{self.new_tc_no}.txt"

    @property
    def new_tc_path(self):
        return f"../Submission/Lab{self.lab}/Testcase/ex{self.lab}_{self.ex}_{self.new_tc_no}.txt"

    def __repr__(self):
        self.preview()
        return ""

    def preview(self) -> None:
        tc = '\n' + self.input if '\n' in self.input else self.input
        answer = '\n' + self.output if '\n' in self.output else self.output
        printf(
            f"LAB{self.lab} EX{self.ex}-{self.tc_no}".center(self.padding, "-"), WHITE)
        printf(f"{CYAN}TESTCASE{WHITE}: {tc if tc else 'No Input'}")
        printf(f"{RED}ANSWER{WHITE}  : {answer if answer else 'No Output'}")

    def read_testcase(self):
        if not os.path.isdir('/'.join(self.tc_path.split('/')[:-1])):
            os.makedirs(self.tc_path)
        if not os.path.isdir('/'.join(self.answer_path.split('/')[:-1])):
            os.makedirs(self.answer_path)
        try:
            with open(self.tc_path, "r") as tc:
                self.input = tc.read()
        except FileNotFoundError:
            with open(self.tc_path, "w") as tc:
                self.is_new = True
        try:
            with open(self.answer_path, "r") as answer:
                self.output = answer.read()
        except FileNotFoundError:
            with open(self.answer_path, "w") as answer:
                self.is_new = True

    def save(self):
        self.delete()
        with open(self.new_tc_path, "w") as tc:
            tc.write(self.input)
        with open(self.new_answer_path, "w") as answer:
            answer.write(self.output)

        self.tc_no = self.new_tc_no

    def delete(self):
        subprocess.run(["rm", self.tc_path])
        subprocess.run(["rm", self.answer_path])


class TestcaseManager:
    def __init__(self, lab: int, ex: int, tc_no: int, start=True):
        self.lab = lab
        self.ex = ex
        self.n = tc_no
        self.changes = set()
        self.testcases = []
        self.padding = 50
        self.read_testcases()
        if start:
            self.program()

    def read_testcases(self) -> None:
        is_new = []
        printf("Current Testcases".center(self.padding, "="), YELLOW)
        for i in range(1, self.n + 1):
            new_tc = Testcase(self.lab, self.ex, i)
            self.testcases.append(new_tc)
            new_tc.preview()
            if new_tc.is_new:
                is_new.append(i)
        printf(f"Complete Reading {len(self.testcases)} Testcases".center(
            self.padding, "="), YELLOW)

        if is_new:
            printf(
                "Some Testcases are Newly Created. Would You Like to Modify Them?[Y,y/N]")

            if input().capitalize() == "Y":
                for i in is_new:
                    modified_tc = self.testcases[i - 1]
                    tc = input(
                        f"[EX{self.ex}-{i}]Enter Testcase Input: ").strip()
                    answer = input(
                        f"[EX{self.ex}-{i}]Enter Testcase Answer: ").strip()

                    modified_tc.input = tc
                    modified_tc.output = answer
                    modified_tc.save()

                printf("=" * self.padding, YELLOW)

    def append_testcase(self) -> None:
        tc = input("Enter Testcase Input: ").strip()
        answer = input("Enter Testcase Answer: ").strip()

        self.n += 1
        new_tc = Testcase(self.lab, self.ex, self.n, tc, answer)
        self.testcases.append(new_tc)
        self.changes.add(self.n)

        printf("Successfully Added!", GREEN)

    def publish(self) -> None:
        if len(self.changes) == 0:
            printf("Nothing to Save")
            return

        printf(
            f"Changes on Testcase #[{', '.join(map(str, list(self.changes)))}] - Total: {len(self.changes)}")
        printf("Are You Sure to Save Changes?[Y,y/N]", end="")
        printf("[It cannot be Undone]", RED)

        if input().capitalize() == "Y":
            for tc in self.testcases:
                tc.save()
            printf("Successfully Saved!", GREEN)
        else:
            printf("To preview changes, press [1]")

        self.changes.clear()

    def modify(self) -> None:
        tc_no = input("Enter Testcase # to Modify: ")
        try:
            tc_no = int(tc_no)
        except:
            printf(f"Enter number between 1 - {self.n}", MAGENTA)
            return

        printf("Current".center(self.padding), YELLOW)
        modified_tc = self.testcases[tc_no - 1]
        modified_tc.preview()
        tc = input("Enter Testcase Input: ").strip()
        answer = input("Enter Testcase Answer: ").strip()

        modified_tc.input = tc
        modified_tc.output = answer
        printf("Modified".center(self.padding), YELLOW)
        modified_tc.preview()

        self.changes.add(tc_no)
        printf("Successfully Modified!", GREEN)

    def delete(self) -> None:
        tc_no = input("Enter Testcase # to Delete: ")
        try:
            tc_no = int(tc_no)
        except:
            printf(f"Enter number between 1 - {self.n}", MAGENTA)
            return

        if tc_no < 1 or tc_no > self.n:
            printf(f"Enter number between 1 - {self.n}", MAGENTA)
            return
        tc = self.testcases[tc_no - 1]

        tc.preview()
        printf("Are You Sure to Delete Testcase Above?[Y,y/N]", end="")
        printf("[It cannot be Undone]", RED)

        if input().capitalize() == "Y":
            self.testcases.pop(tc_no - 1)
            self.n -= 1
            for k, v in enumerate(self.testcases):
                v.new_tc_no = k + 1
            tc.delete()

            self.changes.add("DELETED")
            printf("Successfully Deleted!", GREEN)

    def program(self):
        printf("TESTCASE MANAGER".center(self.padding, "="), CYAN)
        while True:
            try:
                answer = int(
                    input(f"[1]Preview [2]Add [3]Save{f'({len(self.changes)} changes)' if len(self.changes) else ""} [4]Modify [5]Delete [0]Exit: "))
            except:
                printf('-' * self.padding, WHITE)
                continue

            if answer == 0:
                return
            elif answer == 1:
                for tc in self.testcases:
                    tc.preview()
            elif answer == 2:
                self.append_testcase()
            elif answer == 3:
                self.publish()
            elif answer == 4:
                self.modify()
            elif answer == 5:
                self.delete()
            elif answer == 6:
                return
            printf('-' * self.padding, WHITE)


class Grader:
    def __init__(self, lab, ex, tc_no, start=True, cpp=True):
        self.lab = lab
        self.ex = ex
        self.tc_no = tc_no
        self.padding = 50
        self.cpp = cpp
        self.TCManager = TestcaseManager(
            self.lab, self.ex, self.tc_no, start=False)

        printf("AUTOGRADER".center(self.padding, "="), CYAN)

    @property
    def txt_path(self):
        return f"../Scores/Lab{self.lab}/ex{self.lab}_{self.ex}_score.txt"

    @property
    def csv_path(self):
        return f"../Scores/Lab{self.lab}/ex{self.lab}_{self.ex}_score.csv"

    @property
    def submission_dir(self):
        return f"../Submission/Lab{self.lab}/"

    @property
    def score_dir(self):
        return f"../Scores/Lab{self.lab}/"

    def grade(self, recompile=True, save=True):
        if not os.path.isdir(self.score_dir):
            os.makedirs(self.score_dir)
        ext = ".cpp" if self.cpp else ".c"
        compiler = "g++" if self.cpp else "gcc"
        with open(self.txt_path, "w") as test:
            test.write("test")

        scores = []
        testcases = []
        for tc in self.TCManager.testcases:
            testcases.append((tc.input, tc.output))

        for lab_dir in os.listdir(self.submission_dir):
            if lab_dir == "Answer" or lab_dir == "Testcase":
                continue
            printf(f"GRADING ON SESSION : {lab_dir}".center(
                self.padding, "="), MAGENTA)

            for student_id in os.listdir(self.submission_dir + lab_dir):
                result = [student_id]
                printf(f"Checking {CYAN}{student_id}{WHITE}")

                student_path = self.submission_dir + lab_dir + "/" + student_id + "/"
                compile_path = student_path + f"ex{self.lab}_{self.ex}"

                if recompile or not os.path.isfile(compile_path):
                    # Check Submission (cpp file)
                    if not os.path.isfile(compile_path + ext):
                        printf(
                            f"    NO SUBMISSION for ex{self.lab}_{self.ex}", RED)
                        result += ['X', 'No Submission'] * self.tc_no
                        scores.append(result)
                        continue

                    # Compile
                    try:
                        subprocess.run(
                            f"{compiler} {compile_path}*{ext} -o {compile_path}", shell=True, capture_output=True, check=True, text=True)
                    except:
                        printf("    COMPILE ERROR", RED)
                        result += ['X', 'No Submission'] * self.tc_no
                        scores.append(result)
                        continue

                for tc, ans in testcases:
                    output = subprocess.run(
                        [f'{compile_path}'], input=tc, capture_output=True, shell=True, text=True)

                    if output.stderr != "":
                        printf(f"    RUNTIME ERROR: {output.stderror}", RED)
                        result += ['X', "Runtime Error"]

                    if output.stdout.strip() == ans.strip():
                        printf("    CORRECT", GREEN)
                        result += ['O', output.stdout.strip()]
                    else:
                        printf(
                            f"    {RED}RESULT: {output.stdout.strip()} {WHITE}<-> EXPECTED: {ans.strip()}")
                        result += ['X', output.stdout.strip()]
                scores.append(result)
        printf("GRADING COMPLETED".center(self.padding, "="), CYAN)

        if save:
            self.to_csv(scores)
        return scores

    def to_csv(self, data):
        data = pd.DataFrame(data)
        columns = ["Student ID"]
        for i in range(1, self.tc_no + 1):
            columns += [f'TC{self.ex}_{i}', f'ANS{self.ex}_{i}']
        data.columns = columns

        data.to_csv(self.csv_path, index=False)
        printf(f"EXPORTED CSV FILE [{self.csv_path}]")
        return

    def grade_opts(self):
        pass


class ScoreModule:
    def __init__(self):
        try:
            self.lab = int(input("Lab #: "))
        except:
            return

        try:
            self.ex_no = int(input("Total # of EXs: "))
        except:
            return
        self.padding = 50

    def program(self):
        _copyright()
        while True:
            try:
                answer = int(input(
                    "[1]Testcase Manager [2]EX Grader [3]Lab Score Summarizer [4]Exit: "))
            except:
                printf('-' * self.padding)
                continue

            if answer == 1:
                try:
                    ex = int(input("Ex # To Manage: "))
                except:
                    printf('-' * self.padding)
                    continue
                try:
                    tc_no = int(input("# of Testcases: "))
                except:
                    printf('-' * self.padding)
                    continue
                manager = TestcaseManager(self.lab, ex, tc_no)
            elif answer == 2:
                try:
                    ex = int(input("Ex # To Grade: "))
                except:
                    printf('-' * self.padding)
                    continue
                try:
                    tc_no = int(input("# of Testcases: "))
                except:
                    printf('-' * self.padding)
                    continue
                grader = Grader(self.lab, ex, tc_no)
                grader.grade()

            elif answer == 3:
                pass

            elif answer == 4 or answer == 0:
                return

            printf('-' * self.padding, WHITE)


module = ScoreModule()

module.program()
