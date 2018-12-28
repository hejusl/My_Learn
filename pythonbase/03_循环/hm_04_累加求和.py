# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

# 计算0-100累加和
# 定义结果变量
result = 0

i = 0
while i <= 100:
    # print(i)
    # 每一次循环，都让 result 这个变量和 i 这个计数器相加
    result += i
    # 处理计数器
    i += 1
print('0-100累加结果 = %d ' % result)
