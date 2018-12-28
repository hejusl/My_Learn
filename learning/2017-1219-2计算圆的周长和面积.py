# !/usr/local/bin/python3
# coding=utf-8
import math

# 输入圆的半径
r = float(input("请输入圆的半径 r = "))
print("圆的周长 = 2πr = %s*%s*%s = %s" % (2, math.pi, r, 2*math.pi*r))
print("圆的面积 = πr**2 = %s*%s^2 = %s" % (math.pi, r, math.pi*r**2))
print(math.pi*r)

a = float(input("请输入a="))
b = float(input("请输入b="))

# 计算a,b之和与之差的乘积
print("计算a,b之和与之差的乘积")
print((a+b)*(a-b))
# 输入两个数a,b,计算a的b次方再除以b取整后的值
print("计算a的b次方再除以b取整后的值")
print(a**b//b)
