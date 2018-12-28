# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8


def sum_2_num(num1, num2):
    """两个数求和"""
    result = num1 + num2

    # 可以使用返回值，告诉函数调用一方计算结果
    return result


# 可以使用变量，来接收函数执行的返回结果
sum_result = sum_2_num(10, 20)

print('计算结果： %d' % sum_result)

