import os
import os.path
import sys
import subprocess

#input = sys.argv


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
        cmd = subprocess.run(finl_str, shell=True)
        print('Process Completed!!!')
        exit(0)
        return finl_str
    else:
        print("Error in file name!!!")
    exit(1)


if __name__ == '__main__':
    i = input('Script Path\t:')
    inpt_len(i)
