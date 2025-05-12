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
        "GIST", RED, "")
    printf(
        " Computer Programming Assignment Autograder [GS1self.padding1/GS2self.padding8]", WHITE)
    printf("©Yooseung Kim, GIST EECS", YELLOW)


class Testcase:
    def __init__(self, lab, ex, tc_no, tc, answer):
        self.lab = lab
        self.ex = ex
        self.tc_no = tc_no
        self.input = tc
        self.output = answer
        self.padding = 50

    def __repr__(self):
        self.preview()
        return ""

    def preview(self) -> None:
        self.tc = '\n' + self.tc if '\n' in self.tc else self.tc
        answer = '\n' + answer if '\n' in answer else answer
        printf(
            f"LAB{self.lab} EX{self.ex}-{self.tc_no}".center(self.padding, "-"), WHITE)
        printf(f"{CYAN}TESTCASE{WHITE}: {self.input if self.input else 'No Input'}")
        printf(f"{RED}ANSWER{WHITE}  : {self.output if self.output else 'No Output'}")


class TestcaseManager:
    def __init__(self, lab: int, ex: int, tc_no: int):
        self.lab = lab
        self.ex = ex
        self.n = tc_no
        self.changes = set()
        self.testcases = {}
        self.answers = {}
        self.padding = 50
        self.read_testcases()
        self.program()

    def answer_path(self, tc):
        return f"../Submission/Lab{self.lab}/Answer/ex{self.lab}_{self.ex}_{tc}.txt"

    def tc_path(self, tc):
        return f"../Submission/Lab{self.lab}/Testcase/ex{self.lab}_{self.ex}_{tc}.txt"

    def preview(self, tc_no: int) -> None:
        tc = self.testcases[tc_no]
        answer = self.answers[tc_no]
        tc = '\n' + tc if '\n' in tc else tc
        answer = '\n' + answer if '\n' in answer else answer
        printf(
            f"LAB{self.lab} EX{self.ex}-{tc_no}".center(self.padding, "-"), WHITE)
        printf(f"{CYAN}TESTCASE{WHITE}: {tc if answer else 'No Input'}")
        printf(f"{RED}ANSWER{WHITE}  : {answer if answer else 'No Output'}")

    def read_testcases(self) -> None:
        printf("Current Testcases".center(self.padding, "="), YELLOW)
        for i in range(1, self.n + 1):
            try:
                with open(self.answer_path(i), "r") as answer:
                    self.answers[i] = answer.read()
            except FileNotFoundError:
                with open(self.answer_path(i), "w") as answer:
                    self.answers[i] = ""
            try:
                with open(self.tc_path(i), "r") as tc:
                    self.testcases[i] = tc.read()
            except FileNotFoundError:
                with open(self.tc_path(i), "w") as tc:
                    self.testcases[i] = ""

            self.preview(i)
        printf("=" * self.padding, YELLOW)

    def append_testcase(self) -> None:
        tc = input("Enter Testcase Input: ").strip()
        answer = input("Enter Testcase Answer: ").strip()

        self.n += 1
        self.testcases[self.n] = tc
        self.answers[self.n] = answer
        self.changes.add(self.n)

    def publish(self) -> None:
        if len(self.changes) == 0:
            printf("Nothing to Save")
            return

        printf(
            f"Changes on Testcase #[{', '.join(map(str, list(self.changes)))}] - Total: {len(self.changes)}")
        printf("Are You Sure to Save Changes?[Y,y/N]", end="")
        printf("[It cannot be Undone]", RED)

        if input().capitalize() == "Y":
            for i in range(1, self.n + 1):
                with open(self.answer_path(i), "w") as answer:
                    answer.write(self.answers[i])
                with open(self.tc_path(i), "w") as tc:
                    tc.write(self.testcases[i])

            printf("Successfully Saved!", GREEN)
        else:
            printf("To preview changes, press [1]")

        self.changes.clear()

    def modify(self) -> None:
        tc_no = input("Enter Testcase #: ")
        try:
            tc_no = int(tc_no)
        except:
            printf(f"Enter number between 1 - {self.n}", MAGENTA)
            return

        printf("Current".center(self.padding), YELLOW)
        self.preview(tc_no)
        tc = input("Enter Testcase Input: ").strip()
        answer = input("Enter Testcase Answer: ").strip()

        self.testcases[tc_no] = tc
        self.answers[tc_no] = answer
        printf("Modified".center(self.padding), YELLOW)
        self.preview(tc_no)
        self.changes.add(tc_no)

        printf("Successfully Modified!", GREEN)

    def program(self):
        while True:
            try:
                answer = int(
                    input(f"[1]Preview [2]Add [3]Save{f'({len(self.changes)} changes)' if len(self.changes) else ""} [4]Modify [0]Exit: "))
            except:
                printf('-' * self.padding, WHITE)
                continue

            if answer == 0:
                return
            elif answer == 1:
                for i in range(1, self.n + 1):
                    self.preview(i)
            elif answer == 2:
                self.append_testcase()
            elif answer == 3:
                self.publish()
            elif answer == 4:
                self.modify()
            elif answer == 5:
                return
            printf('-' * self.padding, WHITE)


class Grader:
    def __init__(self, ):
        pass


class Summerizer:
    def __init__(self):
        pass


testcase = Testcase(1, 1, 3)
