import os
import subprocess
from typing import Dict, List, Tuple

TOTAL_TASKS = 4
LAB_PATH = "./Lab"
TESTS_PATH = "./Lab_tests"
CORRECT_PATH = "./Lab_correct"


def main():

    # Iterating over all the available lab tasks
    for num_task in range(1, TOTAL_TASKS + 1):

        # Getting the path of a file containing the testcases for the current lab question
        testf = os.path.join(TESTS_PATH, f"{num_task}.txt")

        # Getting the path for the correct lab impl. for the current lab question
        correct_src = os.path.join(CORRECT_PATH, f"{num_task}.c")
        # Getting the path for the student's lab impl. for the current lab question
        lab_src = os.path.join(LAB_PATH, f"{num_task}.c")

        # Generating the input, output pair from the correct impl. against the testcases
        # written in @testf
        test_cases = create_test_cases(testf, correct_src)

        print(f"\n\nTesting Task #{num_task}....\n")

        # Here its checking the student's impl. for the correct lab task
        # by comparing it with the correct impl.
        evaluate_code(test_cases, lab_src)


def compile_code(target: str, src: str) -> Tuple:
    """
    compile_code takes in @src (a .c source file), and compile it into
    a @target executable

    TODO: Error checking using the c_stderr to ensure that the code
    compiles and an exectuable is created. else notify

    """

    cmd = f"gcc -Wall -o {target} {src}"

    process = subprocess.Popen(cmd,
                               bufsize=-1,
                               close_fds=True,
                               shell=True,
                               # preexec_fn=os.setsid,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    (c_stdout, c_stderr) = process.communicate()

    c_status = process.returncode
    return (c_stdout, c_stderr, c_status)


def run_code(executable: str, input_src: str):
    """
    run_code takes in @executable binary to run, while input_src
    is a bytes-string to be pass into the stdin of the program.
    Inputs must be sperated by a \n in the input-src. The \n acts 
    as the Enter key while manually entring the input.
    TODO: add alarm and timer to time execution of program.
        add a kill switch to kill the child process after provided time
        properly format the actual and expected output
    """

    cmd = "./" + executable
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE)

    std_out, std_err = p.communicate(input=input_src)

    return std_out


def create_test_cases(input_src: str, code_src: str) -> List[Dict[str, str]]:
    """
    Every line in the @input_src corresponds to a test case. 
    create_test_cases takes a line at a time as input to the program
    feed it into executable compiled from @code_src and then create a 
    list of inputs and output pairs, this list is the test_cases.
    @code_src must be the correct implementation of the code written by
    the teacher.  
    """

    executable, extension = os.path.splitext(code_src)
    compile_code(executable, code_src)
    testcases = []
    with open(input_src, "r") as file:
        for line in file.readlines():
            input = bytes(line, encoding="utf-8")
            output = run_code(executable, input)
            testcases.append({'input': input, "output": output})

    return testcases


def evaluate_code(testcases: List[Dict[str, str]], code_src: str):
    """
    Runs the Lab codes against the correct code cases and then checks their outputs.
    Prints 'Success' if they satisfy all the test cases successfully else if they fail
    shows them their output and the expected output
    """

    executable, extension = os.path.splitext(code_src)
    compile_code(executable, code_src)
    for testcase in testcases:
        print(f"Testing code for input: {testcase.get('input')}.....")
        curr_output = run_code(executable, testcase.get('input'))
        if curr_output == testcase.get('output'):
            print("Success!")
            print("")
        else:
            print(
                f"Failure!\nExpected Output: \n{testcase.get('output')}\nActual Output: \n{curr_output}")
            print("")


if __name__ == "__main__":
    main()
