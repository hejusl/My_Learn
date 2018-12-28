# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8


def test1():
    print('*' * 50)


def test2():
    print('-' * 50)

    # 函数的嵌套调用
    test1()

    print("-" * 50)


test2()
