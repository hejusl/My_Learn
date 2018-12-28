# !/usr/local/bin/python3
# coding=utf-8

# 1、算术运算符和表达式
'''
 + 加法, - 减法, * 乘法, / 除法, // 整除, % 求余, ** 乘方,
'''
# 1.1 加法
x = 10
y = 20
z = int(x + y)
print(z)

# 1.2 减法
a = 98.45
b = 45.69
c = a - b
print(c)

if c == 52.76:
    print("两数相等!")
else:
    print("两数不等!")

# 判断浮点数是否相等, 使用abs, 满足精度条件
if abs(c - 52.76) < 0.01:
    print("两数相等!")
else:
    print("两束不等!")

# 1.3 乘法
d = a * b
# d的值是 4498.1805
print(d)

# 判断f的值和4498.18的误差小于百分之一
if abs(d-4498.18) < 0.01:
    print("两数相等!")
else:
    print("两数不等!")

# 1.4 除法
e = a/b
print(e)
