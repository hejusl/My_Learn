# !/usr/local/bin/python3.6
# coding=utf-8
from __future__ import print_function
import random
rangeNumber, countNumber, variableNumber = int(input('请输入数值范围>')), int(input('请输入式子的数量>')), int(input('请输入变量的数量>'))
file_path = open('/Users/henry/02_Study/01_Python/learning/计算题.txt', 'w')
# 式子数量
for i in range(countNumber):
    # 生成1至rangeNumber（数值范围）内的正整数
    tmp = random.randint(1, rangeNumber)
    file_path.write(str(tmp))
    # 从1开始循环，循环variableNumber（变量的数量）次
    for j in range(1, variableNumber):
        # 生成-tmp至rangeNumber - tmp内的整数 Ps：永远正整数、负整数各占50%
        newNumber = random.randint(-tmp, rangeNumber - tmp)
        # 自增运算给下一次循环<-tmp>重新赋初始值
        tmp += newNumber
        # 判断newNumber是正整数、负整数以及为0的情况应该怎样打印输出
        if newNumber > 0:
            file_path.write('+' + str(newNumber))
        elif newNumber == 0:
            num = random.randint(0, 1)
            if num == 0:
                file_path.write('+' + str(newNumber))
            else:
                file_path.write('-' + str(newNumber))
        else:
            file_path.write(str(newNumber))
    file_path.write('=\n')
file_path.close()
