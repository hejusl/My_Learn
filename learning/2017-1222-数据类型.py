# !/usr/local/bin/python3
# coding=utf-8
import this
# 2017-12-22, 学习简单数据类型
# 整数类型
# 1237, 0B011, 0X57AF, 0o234
a = 12
b = 0b0110
c = 0x34AF
d = 0o2
print(a, b, c, d)


# 浮点类型
# 3.14159, -2.45e3
e = -2.45e3
print(e)
# 布尔类型
# True, False
f = True
g = False
z = a == b
print(z)

# 可以约定常量全大写
# 变量删除 del
del z
print(z)

# 特殊变量 “_”
x = y = 20
x + y
z = _ + 100

# 1.变量名: 全小写, 可以使用下划线, age, my_var
# 2.常量名: 全大写, 可以使用下划线, LEFT, TAX_RATE
# 3.函数名: 全小写, 可以使用下划线, calculat(), my_func()
# 4.类名: 采用PascalCase命名规则, 即多个单词组成, 每个单词首字母大写, MyClass
# 5.模块/包名: 全小写字母, 可以使用下划线, math, sys
