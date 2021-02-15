import subprocess
import os

TOTAL_TASKS = 4
TEST_PATH = "./Lab"
INPUTS_PATH = "./Lab_inputs"
CORRECT_PATH = "./Lab_correct"

def main():
    
    for num_task in range(1,TOTAL_TASKS + 1):

        inputf = os.path.join(INPUTS_PATH,f"{num_task}.txt")
        correct_src = os.path.join(CORRECT_PATH,f"{num_task}.c")
        test_src = os.path.join(TEST_PATH,f"{num_task}.c")
        
        test_cases = create_test_cases(inputf,correct_src)
        print(f"Testing Task#{num_task}....\n")
        evaluate_code(test_cases,test_src)

"""
compile_code takes in @src (a .c source file), and compile it into
a @target executable

TODO: Error checking using the c_stderr to ensure that the code
compiles and an exectuable is created. else notify

"""

def compile_code(target,src):
    cmd = f"gcc -Wall -o {target} {src}" 

    process = subprocess.Popen(cmd,
                               bufsize=-1,
                               close_fds=True,
                               shell=True,
                               #preexec_fn=os.setsid,
                               stdin  = subprocess.PIPE,
                               stdout = subprocess.PIPE,
                               stderr = subprocess.PIPE)
    
    (c_stdout, c_stderr) = process.communicate()

    c_status =  process.returncode
    return (c_stdout, c_stderr, c_status)


"""
run_code takes in @executable binary to run, while input_src
is a bytes-string to be pass into the stdin of the program.
Inputs must be sperated by a \n in the input-src. The \n acts 
as the Enter key while manually entring the input.
TODO: add alarm and timer to time execution of program.
      add a kill switch to kill the child process after provided time
      properly format the actual and expected output
"""
def run_code(executable,input_src):

    cmd = "./" + executable
    p = subprocess.Popen(cmd, 
                        shell=True,
                        stdout=subprocess.PIPE,
                        stdin=subprocess.PIPE,
                        stderr=subprocess.PIPE)

    std_out, std_err = p.communicate(input=input_src)

    return std_out

"""
Every line in the @input_src corresponds to a test case. 
create_test_cases takes a line at a time as input to the program
feed it into executable compiled from @code_src and then create a 
list of inputs and output pairs, this list is the test_cases.
@code_src must be the correct implementation of the code written by
the teacher.  
"""

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

"""

"""

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



if __name__ == "__main__":
    main()
