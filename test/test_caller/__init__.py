import unittest
import caller


def test_inpt_len(input:str):
    """
    :param input: str(path)
    :return:
    """
    input_len = len(input)
    assert input_len >= 0
    print('Len passed!!!')

    input_type = type(input)
    assert input_type == str
    print('Type passed!!!')

    final_str_type = type("viztracer " + input)
    assert final_str_type == str
    print('Finale output passed!!!')
    exit(0)


if __name__ == '__main__':
    i = input('Script Path\t:')
    try:
        target = __import__(caller.inpt_len(i))
    except ModuleNotFoundError:
        target = "str"
    # test_inpt_len(input('Enter test path:\t'))
    test_inpt_len(target)