# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8
"""
加减法练习题


"""
import random
import operator


n = int(input('输入本次要练习的题目数量：'))
m = int(input('输入练习的数字范围：'))
correct = 0
wrong = 0
# 随机生成2个数字
while (correct + wrong) < n:
    l1 = random.randint(1, m)
    l2 = random.randint(1, (m - l1))
    l3 = [l1, l2]
    l3.sort(reverse=True)
    # l.sort(reverse=True)
    # 随机生成运算符
    op = random.choice("+-")
    # 算正确答案
    if op == "+":
        answer = operator.add(l3[0], l3[1])
    elif op == "-":
        answer = operator.sub(l3[0], l3[1])
    # 和正确答案比较
    result = input("%d %s %d = " % (l3[0], op, l3[1]))
    if result.isdigit():
        result = int(result)
        if result == answer:
            print("\033[1;34m正确\033[0m")
            correct += 1
        else:
            print("\033[1;31m错误，正确答案为：\033[1;32m%d\033[0m" % answer)
            wrong += 1
    else:
        print("\033[1;31m错误，正确答案为：\033[1;32m%d\033[0m" % answer)
        wrong += 1
print("共%d道题，答错%d道" % (n, wrong))


# for i in range(5):
#     # 生成1至rangeNumber（数值范围）内的正整数
#     tmp = random.randint(1, 20)
#     file_path.write(str(tmp))
#     # 从1开始循环，循环variableNumber（变量的数量）次
#     for j in range(1, 2):
#         # 生成-tmp至rangeNumber - tmp内的整数 Ps：永远正整数、负整数各占50%
#         newNumber = random.randint(-tmp, 20 - tmp)
#         # 自增运算给下一次循环<-tmp>重新赋初始值
#         tmp += newNumber
#         # 判断newNumber是正整数、负整数以及为0的情况应该怎样打印输出
#         if newNumber > 0:
#             file_path.write('+' + str(newNumber))
#         elif newNumber == 0:
#             num = random.randint(0, 1)
#             if num == 0:
#                 file_path.write('+' + str(newNumber))
#             else:
#                 file_path.write('-' + str(newNumber))
#         else:
#             file_path.write(str(newNumber))
#     file_path.write('=\n')
# file_path.close()
