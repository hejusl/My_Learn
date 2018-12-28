# !/usr/local/bin/python3
# coding=utf-8
from __future__ import print_function
import random
rangeNumber, countNumber, variableNumber = int(input('请输入数值范围>')), int(input('请输入式子的数量>')), int(input('请输入变量的数量>'))
for i in range(countNumber):
    tmp = random.randint(1, rangeNumber)
    print(tmp, end='')
    for j in range(1, variableNumber):
        newNumber = random.randint(-tmp, rangeNumber - tmp)
        tmp += newNumber
        print('%+d' % (newNumber,), end='')
    print()
