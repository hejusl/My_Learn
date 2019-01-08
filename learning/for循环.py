# !/usr/local/bin/python
# coding=utf-8
import random

# for letter in 'Python':
#     print('当前字母：', letter)
# print()
#
# fruits1 = ['banana', 'apple', 'mango']
# for fruit1 in fruits1:
#     print('当前水果：', fruit1)
# print('Good bye!')
# print()
#
# # 索引迭代
# fruits2 = ['banana', 'apple', 'mango']
# for index in range(len(fruits2)):
#     print('当前水果：', fruits2[index])
# print('Good bye!')
# print()
#
# # 循环使用else语句
# for num in range(10, 20):       # 迭代 10 到 20 之间的数字
#     for i in range(2, num):     # 根据因子迭代
#         if num % i == 0:        # 确定第一个因子
#             j = num / i         # 计算第二个因子
#             print('%d 等于 %d * %d' % (num, i, j))
#             break               # 跳出当前循环
#     else:
#         print(num, '是一个质数')

l1 = random.randint(1, 20)
l2 = random.randint(1, (20 - l1))
l3 = [l1, l2]
l3.sort(reverse=True)
print(l1)
print(l2)
print(l3)
# n = sum(l1)
# l1.sort(reverse=True)
# print(l1)




# for i in range(0,5000):
#     x = random.randint(0,9)
#     y = random.randint(0,9)
#     if x!=y:
#         randl[x], randl[y] = randl[y], randl[x]
# print(randl)