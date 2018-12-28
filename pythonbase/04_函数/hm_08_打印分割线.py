# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8


def print_line1():
    """打印 * 组成的分割线"""

    print("*" * 50)


print_line1()


def print_line2(char):
    """打印任意字符组成的分割线"""

    print(char * 50)


print_line2("-")


def print_line3(char, time):
    """打印任意重复次数的分割线"""

    print(char * time)


print_line3("A", 50)


