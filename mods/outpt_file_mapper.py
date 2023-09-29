import os
import sys


class File_Mapper:
    def __init__(self, filename_str, curr_dir, file_name_op):
        self.filename = filename_str
        self.curr_dir = curr_dir
        self.file_name_op = file_name_op

        self.result_dir = os.path.join(self.curr_dir, 'Results')

    def get_project_dir(self):
        if os.path.isfile(self.filename):
            file_name = os.path.basename(self.filename)
            if not os.path.abspath(self.filename):
                file_name1 = '\\' + os.path.join(self.filename.split('\\')[0:-1])
                print(f'Not An Absolute Path!!!')
            else:
                file_name_1 = os.path.split(os.path.abspath(self.filename))
                file_name1 = file_name_1[0].replace('\\', '__').replace(':', '_')
                file_name2 = file_name_1[1].replace('.', '_')
                fin_file_name = file_name1 + file_name2
                print('get_proj_dir -- 1: \t', fin_file_name)
                return fin_file_name

    def make_output_dir_file(self):
        if os.path.exists(self.result_dir):
            path = os.path.join(self.result_dir, self.file_name_op)
            os.mkdir(path)
            print("Created Directory:\t", path)
            return path
        else:
            os.mkdir(self.result_dir)
            print('base result Dir was not present.>>')
            path = os.path.join(self.result_dir, self.file_name_op)
            os.mkdir(path)
            print("Created Directory:\t", path)
            return path
