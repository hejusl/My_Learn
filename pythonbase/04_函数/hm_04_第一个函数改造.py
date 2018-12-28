# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

# 是定义好函数之后，只表示这个函数封装了一段代码
# 如果不主动调用函数，函数是不主动执行的
name = '小明'


def say_hello():
    """打招呼"""
    print('hello 1')
    print('hello 2')
    print("hello 3")


print(name)

say_hello()

print(name)
