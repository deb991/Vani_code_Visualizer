import os
import os.path
import sys
import subprocess
# from side_load import nl

from mods.outpt_file_mapper import File_Mapper


cur_dir = os.getcwd()
file_name = input('Enter File name Dir:\t')
file_mapper_obj = File_Mapper(file_name, cur_dir, 'xyz')


class ScriptCaller:
    def __init__(self):
        self.filename_input = file_name

    def get_fin_str(self):
        input_len = len(self.filename_input)
        input_type = type(self.filename_input)
        # print(f'\t{input_len}, \t{input_type}')
        # file_name1 = file_mapper_obj.get_project_dir(self.filename_input)
        file_name1 = file_mapper_obj.get_project_dir()

        cur_dir = os.getcwd()
        os.chdir(cur_dir)

        output_path = file_mapper_obj.make_output_dir_file()
        output_file = f"{file_name1}+.html"

        # print(f"Outfile Path:\t{output_path}, Output_file:\t{output_file}")

        dir_str = f"{output_path}//{output_file}"
        file_path = os.path.join(dir_str)
        # print('File_path:\t', file_path)

        if input_len != 0 and input_type == str:
            try:
                file_name = self.filename_input
                # print('File Name__1:\t', file_name)
                finl_str = "viztracer -o " + file_path + ' ' + file_name
                # print("File Name:\t", finl_str)
                os.chdir(cur_dir)
                cmd = subprocess.run(finl_str, shell=True)
                # print('Process Completed!!!')
                return finl_str
            except FileNotFoundError:
                pass
        else:
            print("Error in file name!!!")


if __name__ == '__main__':
    script = ScriptCaller()
    script.get_fin_str()
