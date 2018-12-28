# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

# 在控制台连续输出5行 * ，每一行星号数量依次递增
# *
# **
# ***
# ****
# *****
# 1、 定义一个计数器变量，从数字1开始循环比较方便
row = 1

# 2、 开始循环

while row <= 5:
    print('*' * row)
    row += 1
