# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

# 在控制台连续输出5行 * ，每一行星号数量依次递增
# *
# **
# ***
# ****
# *****
# 1、 完成 5 行内容的简单输出
# 2、 分析每行内部的 * 应该如何处理


def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print('%d x %d = %d' % (col, row, row * col), end='\t')
            col += 1
        print('')
        row += 1
