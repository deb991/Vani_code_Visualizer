import os
import os.path
import sys
import subprocess
# from side_load import nl

from mods.outpt_file_mapper import get_proj_dir, make_output_dir_file


def inpt_len(input: str):
    """
    :param input: any
    :return: str
    """
    input_len = len(input)
    input_type = type(input)
    file_name1 = get_proj_dir(input)

    cur_dir = os.getcwd()
    os.chdir(cur_dir)

    output_path = make_output_dir_file(cur_dir, file_name1)
    output_file = f"{file_name1}+.html"

    print(f"Outfile Path:\t{output_path}, Output_file:\t{output_file}")

    dir_str = f"{output_path}//{output_file}"
    file_path = os.path.join(dir_str)
    print('File_path:\t', file_path)

    if input_len != 0 and input_type == str:
        file_name = input
        print('File Name__1:\t', file_name)
        finl_str = "viztracer -o " + file_path + ' ' + file_name
        # print("File Name:\t", finl_str)
        cmd = subprocess.run(finl_str, shell=True)
        print('Process Completed!!!')
        return finl_str
    else:
        print("Error in file name!!!")


if __name__ == '__main__':
    i = input('Script Path\t:')
    inpt_len(i)
