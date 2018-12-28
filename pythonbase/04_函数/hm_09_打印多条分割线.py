# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8


def print_line(char, times):
    """打印任意重复次数的分割线
    :param char:
    :param times:
    """

    print(char * times)


def print_lines(char, times):
    """打印多条分割线
    :param char: 分割字符
    :param times: 分割线重复次数
    """
    row = 0

    while row < 5:

        print_line(char, times)

        row += 1


print_lines("-", 20)

