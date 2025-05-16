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
DEFAULT = '\\e[0m'


def BOLD(color):
    return color.replace('0;', '1;')


def UNDERLINE(color):
    return color.replace('0;', '4;')


def BACKGROUND(color):
    return color.replace('0;3', '4')


def printf(string: str, color: str = "", end: str = "\n") -> None:
    os.system(f'printf "{color}{string}{end}{DEFAULT}"')


def _copyright():
    printf(
        f"{RED}GIST {DEFAULT}Computer Programming Assignment Autograder [GS1401/GS2408]")
    printf("©Yooseung Kim, GIST EECS".rjust(60), BLUE)


class Testcase:
    def __init__(self, lab, ex, tc_no, tc_dir, answer_dir, tc="", answer="", padding=50, main_color=BLUE, alt_color=YELLOW, error_color=RED, warning_color=MAGENTA):
        self.lab = lab
        self.ex = ex
        self.tc_no = tc_no
        self.new_tc_no = tc_no
        self.input = tc
        self.output = answer
        self.padding = padding
        self.is_new = False
        self.tc_dir = tc_dir
        self.answer_dir = answer_dir
        self.main_color = main_color
        self.alt_color = alt_color
        self.error_color = error_color
        self.warning_color = warning_color
        self.read_testcase()

    @property
    def answer_path(self):
        return f"{self.answer_dir}/ex{self.lab}_{self.ex}_{self.tc_no}.txt"

    @property
    def tc_path(self):
        return f"{self.tc_dir}/ex{self.lab}_{self.ex}_{self.tc_no}.txt"

    @property
    def new_answer_path(self):
        return f"{self.answer_dir}/ex{self.lab}_{self.ex}_{self.new_tc_no}.txt"

    @property
    def new_tc_path(self):
        return f"{self.tc_dir}/ex{self.lab}_{self.ex}_{self.new_tc_no}.txt"

    def __repr__(self):
        self.preview()
        return ""

    def preview(self) -> None:
        tc = '\n' + self.input if '\n' in self.input else self.input
        answer = '\n' + self.output if '\n' in self.output else self.output
        printf(
            f"LAB{self.lab} EX{self.ex}-{self.tc_no}".center(self.padding, "-"), DEFAULT)
        printf(f"{self.main_color}TESTCASE{DEFAULT}: {tc if tc else 'No Input'}")
        printf(
            f"{self.alt_color}ANSWER{DEFAULT}  : {answer if answer else 'No Output'}")

    def read_testcase(self):
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
    def __init__(self, lab: int, ex: int, tc_dir, answer_dir, start=True, padding: int = 50, main_color=BLUE, alt_color=YELLOW, good_color=GREEN, error_color=RED, warning_color=MAGENTA):
        self.lab = lab
        self.ex = ex
        self.tc_dir = tc_dir
        self.answer_dir = answer_dir
        self.n = self.check_tc()
        self.new = False
        self.changes = set()
        self.testcases = []
        self.padding = padding
        self.main_color = main_color
        self.alt_color = alt_color
        self.good_color = good_color
        self.error_color = error_color
        self.warning_color = warning_color
        self.read_testcases()
        if start:
            self.program()

    def check_tc(self):
        output = list(
            filter(lambda x: f"ex{self.lab}_{self.ex}_" in x, os.listdir(self.tc_dir)))
        return len(output)

    def read_testcases(self) -> None:
        if self.n == 0:
            printf("Created New Exercise", self.main_color)
            try:
                self.n = int(input("Enter # of TC to Create: "))
                assert self.n > 0
            except:
                printf("Invalid Number Given, Creating 3 TC as Default",
                       self.warning_color)
                self.n = 3

            for i in range(1, self.n + 1):
                tc = input(
                    f"[EX{self.ex}-{i}]Enter Testcase Input: ").strip()
                answer = input(
                    f"[EX{self.ex}-{i}]Enter Testcase Answer: ").strip()

                new_tc = Testcase(self.lab, self.ex, i, self.tc_dir,
                                  self.answer_dir, tc=tc, answer=answer, padding=self.padding)
                self.testcases.append(new_tc)

            printf("=" * self.padding, self.main_color)
            self.new = True
            return

        printf("Current Testcases".center(self.padding, "="), self.alt_color)
        for i in range(1, self.n + 1):
            new_tc = Testcase(self.lab, self.ex, i, self.tc_dir,
                              self.answer_dir, padding=self.padding)
            self.testcases.append(new_tc)
            new_tc.preview()

        printf(f"Complete Reading {len(self.testcases)} Testcases".center(
            self.padding, "="), self.alt_color)

    def append_testcase(self) -> None:
        tc = input("Enter Testcase Input: ").strip()
        answer = input("Enter Testcase Answer: ").strip()

        self.n += 1
        new_tc = Testcase(self.lab, self.ex, self.n, self.tc_dir,
                          self.answer_dir, tc, answer,  self.padding)
        new_tc.save()
        self.testcases.append(new_tc)

        printf("Successfully Added!", self.good_color)

    def publish(self) -> None:
        if len(self.changes) == 0:
            printf("Nothing to Save")
            return

        printf(
            f"Changes on Testcase #[{', '.join(map(str, list(self.changes)))}] - Total: {len(self.changes)}")
        printf("Are You Sure to Save Changes?[Y,y/N]", end="")
        printf("[It cannot be Undone]", self.warning_color)

        if input().capitalize() == "Y":
            for tc in self.testcases:
                tc.save()
            printf("Successfully Saved!", self.good_color)
        else:
            printf("To preview changes, press [1]")

        self.changes.clear()

    def modify(self) -> None:
        tc_no = input("Enter Testcase # to Modify: ")
        try:
            tc_no = int(tc_no)
        except:
            printf(f"Enter number between 1 - {self.n}", self.error_color)
            return

        printf("Current".center(self.padding, "="), self.alt_color)
        modified_tc = self.testcases[tc_no - 1]
        modified_tc.preview()
        tc = input("Enter Testcase Input: ").strip()
        answer = input("Enter Testcase Answer: ").strip()

        modified_tc.input = tc
        modified_tc.output = answer
        printf("Modified".center(self.padding), self.alt_color)
        modified_tc.preview()

        self.changes.add(tc_no)
        printf("Successfully Modified!", self.good_color)

    def delete(self) -> None:
        tc_no = input("Enter Testcase # to Delete: ")
        try:
            tc_no = int(tc_no)
        except:
            printf(f"Enter number between 1 - {self.n}", self.error_color)
            return

        if tc_no < 1 or tc_no > self.n:
            printf(f"Enter number between 1 - {self.n}", self.error_color)
            return
        tc = self.testcases[tc_no - 1]

        tc.preview()
        printf("Are You Sure to Delete Testcase Above?[Y,y/N]", end="")
        printf("[It cannot be Undone]", self.warning_color)

        if input().capitalize() == "Y":
            self.testcases.pop(tc_no - 1)
            self.n -= 1
            for k, v in enumerate(self.testcases):
                v.new_tc_no = k + 1
            tc.delete()

            self.changes.add("DELETED")
            printf("Successfully Deleted!", self.good_color)

    def program(self):
        printf("TESTCASE MANAGER".center(self.padding, "="), self.main_color)
        while True:
            try:
                answer = int(
                    input(f"[1]Preview [2]Add [3] Modify [4]Save{f'({len(self.changes)} changes)' if len(self.changes) else ""} [5]Delete [6/0]Exit: "))
            except:
                printf('_' * self.padding, DEFAULT)
                continue

            if answer == 0:
                return
            elif answer == 1:
                for tc in self.testcases:
                    tc.preview()
            elif answer == 2:
                self.append_testcase()
            elif answer == 3:
                self.modify()
            elif answer == 4:
                self.publish()
            elif answer == 5:
                self.delete()
            elif answer == 6:
                return
            printf('_' * self.padding, DEFAULT)


class Grader:
    def __init__(self, lab, ex, submission_dir, tc_dir, answer_dir, score_dir, padding: int = 50, main_color=BLUE, alt_color=CYAN, good_color=GREEN, error_color=RED, warning_color=MAGENTA, recompile=False, cpp=True):
        self.lab = lab
        self.ex = ex
        self.padding = padding
        self.cpp = cpp
        self.submission_dir = submission_dir
        self.tc_dir = tc_dir
        self.answer_dir = answer_dir
        self.score_dir = score_dir
        self.tc_no = self.check_tc()
        self.main_color = main_color
        self.alt_color = alt_color
        self.good_color = good_color
        self.alt_color = alt_color
        self.error_color = error_color
        self.warning_color = warning_color
        self.points = 10
        self.recompile = recompile
        self.std = 'c++11' if cpp else 'c11'
        self.TCManager = TestcaseManager(
            self.lab, self.ex, self.tc_dir, self.answer_dir, start=False, padding=self.padding)
        printf("AUTOGRADER".center(self.padding, "="), self.main_color)

    @property
    def csv_path(self):
        return f"{self.score_dir}/ex{self.lab}_{self.ex}_score.csv"

    def check_tc(self):
        output = list(
            filter(lambda x: f"ex{self.lab}_{self.ex}_" in x, os.listdir(self.tc_dir)))
        return len(output)

    def grade(self, save=True):
        if not os.path.isdir(self.score_dir):
            os.makedirs(self.score_dir)

        self.show_grade_ops()
        while input("Confirm Grading Options?[Y,y/N]: ").strip().capitalize() != "Y":
            self.set_grade_opts()
            self.show_grade_ops()

        printf(f"Now Grading Lab{self.lab} Ex{self.ex}", self.main_color)
        ext = ".cpp" if self.cpp else ".c"
        compiler = "g++" if self.cpp else "gcc"
        scores = []
        testcases = []
        for tc in self.TCManager.testcases:
            testcases.append((tc.input, tc.output))

        for lab_dir in os.listdir(self.submission_dir):
            if lab_dir == "Answer" or lab_dir == "Testcase":
                continue
            printf(f"GRADING ON SESSION : {lab_dir}".center(
                self.padding, "="), self.main_color)

            for student_id in os.listdir(f"{self.submission_dir}/{lab_dir}"):
                result = [lab_dir, student_id]
                printf(
                    f"Checking {self.alt_color}{student_id}{DEFAULT}")

                student_path = f"{self.submission_dir}/{lab_dir}/{student_id}"
                compile_path = f"{student_path}/ex{self.lab}_{self.ex}"

                if self.recompile or not os.path.isfile(compile_path):
                    # Check Submission (cpp file)
                    if not os.path.isfile(compile_path + ext):
                        printf(
                            f"    NO SUBMISSION for ex{self.lab}_{self.ex}", self.error_color)
                        result += ['X', 'No Submission'] * self.tc_no + [0]
                        scores.append(result)
                        continue

                    # Compile
                    try:
                        subprocess.run(
                            f"{compiler} -std={self.std} {compile_path}*{ext} -o {compile_path}", shell=True, capture_output=True, check=True, text=True)
                    except:
                        printf("    COMPILE ERROR", self.error_color)
                        result += ['X', 'No Submission'] * self.tc_no + [0]
                        scores.append(result)
                        continue

                correct = True
                for tc, ans in testcases:
                    output = subprocess.run(
                        [f'{compile_path}'], input=tc, capture_output=True, shell=True, text=True)

                    if output.stderr != "":
                        printf(
                            f"    RUNTIME ERROR: {output.stderror}", self.error_color)
                        result += ['X', "Runtime Error"]

                    if output.stdout.strip() == ans.strip():
                        printf("    CORRECT", self.good_color)
                        result += ['O', output.stdout.strip()]
                    else:
                        printf(
                            f"    {self.error_color}RESULT: {output.stdout.strip() if output.stdout else 'ø'} {DEFAULT}<-> EXPECTED: {ans.strip() if ans else 'ø'}")
                        result += ['X', output.stdout.strip()]
                        correct = False
                result += [self.points if correct else 0]
                scores.append(result)
        printf("GRADING COMPLETED".center(self.padding, "="), self.main_color)

        if len(scores) == 0:
            printf(
                f"Could not find submissions. Make sure submissions are in the directory [{UNDERLINE(GRAY)}{self.submission_dir}/{self.warning_color}]", self.warning_color)
            return scores

        if save:
            self.to_csv(scores)
        return scores

    def to_csv(self, data):
        data = pd.DataFrame(data)
        columns = ["Session #", "Student ID"]
        for i in range(1, self.tc_no + 1):
            columns += [f'TC{self.ex}_{i}', f'ANS{self.ex}_{i}']
        columns += [f'Points{self.ex}']
        data.columns = columns

        data.to_csv(self.csv_path, index=False)
        printf(
            f"{self.good_color}EXPORTED CSV FILE [{UNDERLINE(GRAY)}{self.csv_path}{self.good_color}]")
        return

    def show_grade_ops(self):
        printf(f"Points: {self.main_color}{self.points}{DEFAULT}, Compiler: {self.alt_color}{"g++" if self.cpp else "gcc"}{DEFAULT}, C/C++: -std={self.std}, Recompile: {self.alt_color}{self.recompile}")

    def set_grade_opts(self):
        printf(
            f"Enter options separated by comma, e.g. {self.main_color}'points=#, compiler=gcc, -std=c11, recompile=false'")
        try:
            answer = input(
                "Case INsensitive, may omit options to use default: ").split(',')

            opts = dict(arg.split("=") for arg in answer)

            if "points" in opts.keys():
                self.points = int(opts["points"])
            if "compiler" in opts.keys():
                self.cpp = False if opts['compiler'].strip(
                ).lower() == "gcc" else True
                if self.cpp:
                    self.std = 'c++11'
                else:
                    self.std = 'c11'
            if "recompile" in opts.keys():
                self.recompile = False if opts['recompile'].strip(
                ).lower() == "false" else True

            if "-std" in opts.keys() or 'std' in opts.keys():
                self.std = opts.get('-std', opts.get('std', "c++11"))

            if (self.cpp and "++" not in self.std) or (not self.cpp and "++" in self.std):
                printf(
                    f"Compiler({'g++' if self.cpp else 'gcc'}) and C/C++ standard(-std={self.std}) does not match", self.warning_color)
        except:
            if len(answer) == 0:
                return
            printf("Invalid Input", self.error_color)
        return


class Summarizer:
    def __init__(self, lab, score_dir, padding=50, main_color=BLUE, alt_color=CYAN, good_color=GREEN, error_color=RED, warning_color=MAGENTA):
        self.lab = lab
        self.padding = padding
        self.score_dir = score_dir
        self.main_color = main_color
        self.alt_color = alt_color
        self.good_color = good_color
        self.error_color = error_color
        self.warning_color = warning_color

    def export_data(self):
        if not os.path.isdir(self.score_dir):
            printf("Directory Does Not Exist. Please Grade Scores First.",
                   self.error_color)

        scores = pd.DataFrame(
            columns=['Session #', 'Student ID', 'Total Points'])
        printf("Reading Score Data", CYAN)
        suffix = 1
        files = subprocess.run(f"ls {self.score_dir}/ex{self.lab}_*_score.csv",
                               shell=True, capture_output=True, text=True).stdout.split('\n')
        for ex in files:
            if ex == "":
                continue
            scores = pd.merge(scores, pd.read_csv(ex)[['Session #', 'Student ID', f'Points{suffix}']], on=[
                'Session #', 'Student ID'], how='outer')
            suffix += 1

        if suffix == 1:
            printf("No Data Found, Please Grade First", self.warning_color)
            return pd.DataFrame()
        scores['Total Points'] = sum(
            scores[f'Points{i}'] for i in range(1, suffix))
        scores.to_csv(f"{self.score_dir}/Lab{self.lab}.csv", index=False)
        printf(
            f"{self.good_color}Successfully Exported Summary [{UNDERLINE(GRAY)}{self.score_dir}/Lab{self.lab}.csv{self.good_color}]")

        self.review_data(scores)
        return scores

    def review_data(self, data):
        printf(f"SUMMARY".center(self.padding, "="), self.main_color)
        print(data.groupby('Session #').describe())


class ScoreModule:
    def __init__(self, lab, main_color=BOLD(BLUE), tc_color=YELLOW, grader_color=CYAN, summary_color=CYAN,  good_color=GREEN, error_color=RED, warning_color=MAGENTA, padding=60, cpp=True, recompile=False):
        self.lab = lab
        self.padding = int(padding)
        self.main_color = main_color
        self.tc_color = tc_color
        self.grader_color = grader_color
        self.summary_color = summary_color
        self.good_color = good_color
        self.error_color = error_color
        self.warning_color = warning_color
        self.cwd = os.getcwd()
        self.check_dir()
        self.ex = self.check_ex()
        self.cpp = cpp
        self.recompile = recompile

    @property
    def submission_dir(self):
        return f"{self.cwd}/Submission/Lab{self.lab}"

    @property
    def answer_dir(self):
        return f"{self.submission_dir}/Answer"

    @property
    def tc_dir(self):
        return f"{self.submission_dir}/Testcase"

    @property
    def score_dir(self):
        return f"{self.cwd}/Scores/Lab{self.lab}"

    def check_dir(self):
        if not os.path.isdir(self.answer_dir):
            os.makedirs(self.answer_dir)

        if not os.path.isdir(self.tc_dir):
            os.makedirs(self.tc_dir)

        if not os.path.isdir(self.score_dir):
            os.makedirs(self.score_dir)

    def check_ex(self):
        try:
            tcs = len(
                set(map(lambda x: x.split("_")[1], os.listdir(self.tc_dir))))
            answers = len(
                set(map(lambda x: x.split("_")[1], os.listdir(self.answer_dir))))
        except IndexError:
            printf(
                f"Name of TC and Answer Files should be form of {self.error}ex#_#")

        ex = min(tcs, answers)

        if tcs != answers:
            printf(
                f"Assuming {ex} Exercises (Given {tcs} from TC / {answers} from ANS)", self.warning_color)

        return ex

    def program(self):
        _copyright()
        printf(
            f"Grading On: {self.main_color}LAB{self.lab}{DEFAULT}[{self.main_color}{self.ex} {DEFAULT}Exercises]")
        while True:
            try:
                answer = int(input(
                    "[1]Testcase Manager [2]EX Grader [3]Lab Score Summarizer [4/0]Exit: "))
            except:
                printf('_' * self.padding)
                continue

            if answer == 1:
                try:
                    ex = int(
                        input(f"Ex # To Manage (or Create)[{self.ex} EX Existing]: "))
                    assert ex > 0
                except:
                    printf('_' * self.padding)
                    continue

                ex = min(ex, self.ex + 1)
                manager = TestcaseManager(
                    self.lab, ex, self.tc_dir, self.answer_dir, padding=self.padding, main_color=self.main_color, alt_color=self.tc_color)
                self.ex += 1 if manager.new else 0
            elif answer == 2:
                if self.ex == 0:
                    printf(f"Add Exercises First", self.error_color)
                    continue
                try:
                    ex = int(input(f"Ex # To Grade [{self.ex} EX]: "))
                    if ex > self.ex or ex < 1:
                        printf(
                            f"Enter Ex # between 1 and {self.ex}", self.error_color)
                        printf('_' * self.padding)
                        continue
                except:
                    printf('_' * self.padding)
                    continue
                grader = Grader(self.lab, ex, self.submission_dir, self.tc_dir, self.answer_dir,
                                self.score_dir, padding=self.padding, main_color=self.main_color, alt_color=self.grader_color, cpp=self.cpp, recompile=self.recompile)
                grader.grade()

            elif answer == 3:
                summary = Summarizer(
                    self.lab, self.score_dir, self.padding, main_color=self.main_color, alt_color=self.summary_color)
                summary.export_data()
            elif answer == 4 or answer == 0:
                return

            printf('_' * self.padding)


def main(lab, **kwargs):
    main_color = BOLD(BLUE)
    tc_color = YELLOW
    grader_color = CYAN
    summary_color = CYAN
    module = ScoreModule(lab, main_color=main_color, tc_color=tc_color,
                         grader_color=grader_color, summary_color=summary_color, **kwargs)
    module.program()


if __name__ == "__main__":
    lab = sys.argv[1]
    # kwargs for ScoreModule: padding, main_color, alt_color, warning_color, error_color
    kwargs = dict(arg.split("=") for arg in sys.argv[2:])

    main(lab, **kwargs)
