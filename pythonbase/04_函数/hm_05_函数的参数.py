# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

# 是定义好函数之后，只表示这个函数封装了一段代码
# 如果不主动调用函数，函数是不主动执行的


def sum_2_num(num1, num2):
    """两个数字的求和"""
    # num1 = 10
    # num2 = 20

    result = num1 + num2

    print('%d + %d = %d' % (num1, num2, result))


sum_2_num(50, 20)
