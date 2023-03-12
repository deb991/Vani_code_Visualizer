import os
import os.path
import sys
import subprocess

inpt = sys.argv


def inpt_len(input: os.path):
    """
    :param input: any
    :return: str
    """
    input_len = len(input)
    input_type = type(input)
    if input_len != 0 and input_type == str:
        file_name = input
        print('File Name__1:\t', file_name)
        finl_str = f"viztracer " + file_name
        print("File Name:\t", finl_str)
        subprocess.run(finl_str, shell=True)
        print('Process Completed!!!')
        #if os.path.isfile(file_name):
        #    subprocess.call(["viztracer", f" {file_name}"])
        return finl_str
    else:
        print("Error in file name!!!")
    exit(0)

if __name__ == '__main__':
    try:
        i = input()
        inpt_len(i)
    except:
        try:
            i = sys.argv[0]
            inpt_len(i)
        except:
            print("Input not correct!!!")
