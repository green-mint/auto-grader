import subprocess
import os

def compile_code(target,src):
    cmd = f"gcc -Wall -o {target} {src}"
    process = subprocess.Popen(cmd,bufsize=-1,
                                close_fds=True,
                                shell=True,
                                preexec_fn=os.setsid,
                                stdin  = subprocess.PIPE,
                                stdout = subprocess.PIPE,
                                stderr = subprocess.PIPE)
    
    (c_stdout, c_stderr) = process.communicate()

    c_status =  process.returncode
    return (c_stdout, c_stderr, c_status)


def run_code(executable,input_src):

    p = subprocess.Popen(["./" + executable], 
                        shell=True,
                        stdout=subprocess.PIPE,
                        stdin=subprocess.PIPE)

    std_out, std_err = p.communicate(input=input_src)

    return std_out

def create_test_cases(input_src,code_src):
    executable, extension = os.path.splitext(code_src)
    compile_code(executable,code_src)
    testcases = []
    with open(input_src,"r") as file:
        for line in file.readlines():
            input = bytes(line,encoding="utf-8")
            output = run_code(executable, input)
            testcases.append([input,output])
    return testcases

def evaluate_code(testcases, code_src):
    executable, extension = os.path.splitext(code_src)
    compile_code(executable,code_src)
    for test_case in testcases:
        print(f"Testing code for input: {test_case[0]}.....")
        output = run_code(executable,test_case[0])
        if output == test_case[1]:
            print("Success!")
            print("")
        else:
            print(f"Failure!\nExpected Output: {test_case[1]}\nActual Output: {output}")
            print("")

TOTAL_TASKS = 4
TEST_PATH = "./Lab3"
INPUTS_PATH = "./Lab3_inputs"
CORRECT_PATH = "./Lab3_correct"

for num_task in range(1,TOTAL_TASKS + 1):

    inputf = os.path.join(INPUTS_PATH,f"{num_task}.txt")
    correct_src = os.path.join(CORRECT_PATH,f"{num_task}.c")
    test_src = os.path.join(TEST_PATH,f"{num_task}.c")
    
    test_cases = create_test_cases(inputf,correct_src)
    print(f"Testing Task#{num_task}....\n")
    evaluate_code(test_cases,test_src)
