# !/usr/local/bin/python
# coding=utf-8

x = int(input("x="))
y = int(input("y="))
# 打印x+y的结果
print("x+y = %d+%d = %d" % (x, y, x+y))

# 打印x-y的结果
print("x-y = %d-%d = %d" % (x, y, x-y))

# 打印x的y次方
print("x的y次方 = %d^%d = %d" % (x, y, x**y))

# 打印x除以y的结果
print("x/y = %d/%d = %d" % (x, y, x/y))

# 除后取整，x//y
print("87/5的整数部分 = %d" % (87//5))

# 取余数，x%y
print("x/y的余数= %d/%d = %d" % (x, y, x % y))
