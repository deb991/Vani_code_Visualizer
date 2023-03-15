import os
import sys


def get_proj_dir(filename: os.path):
    if os.path.isfile(filename):
        file_name = os.path.basename(filename)
        if not os.path.abspath(filename):
            file_name1 = '\\'+ os.path.join(filename.split('\\')[0:-1])
        else:
            file_name_1 = os.path.split(os.path.abspath(filename))
            file_name1 = file_name_1[0].replace('\\', '__').replace(':', '_')
            file_name2 = file_name_1[1].replace('.', '_')
            fin_file_name = file_name1 + file_name2
            print('get_proj_dir -- 1: \t', fin_file_name)
        return fin_file_name


def make_output_dir_file(result_path: any, file_name: str):
    """
    :param result_path: path where resut output will be stored.
    :param file_name: Project/ test result file name based on input file name.
    :return: path
    """
    cur_dir = os.getcwd()
    result_dir = os.path.join(cur_dir, 'Results')
    if os.path.exists(result_dir):
        path = os.path.join(result_dir, file_name)
        os.mkdir(path)
        print("Created Directory:\t", path)
        return path
    else:
        os.mkdir(result_dir)
        print('base result Dir was not present.>>')
        path = os.path.join(result_dir, result_path)
        os.mkdir(path)
        print("Created Directory:\t", path)
        return path


if __name__ == '__main__':
    file_name = get_proj_dir()
    make_output_dir_file()