# !/usr/local/bin/python3
# coding=utf-8

# 定义a列表
a = ['a', 'b', 3]
# 定义b列表
b = [1, 2, 'c']
# 定义c列表,它是a和b的嵌套
c = [a, b]
# 打印c列表,它包含两个元素,分别是a列表,b列表
print(c)
# 打印c列表的第一个元素,即a列表
print(c[0])
# 打印c列表的第一个元素中的第三个元素
print(c[0][2])

c.append(5)
print(c)
