# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

# 计算 0-100 之间 所有的 偶数 求和
# 开发步骤
# 编写循环 确认要计算的数字
# 添加 结果 变量，在循环内部 处理计算结果
i = 0
result = 0
while i <= 100:
    # 判断变量i重的数值是否是偶数
    if i % 2 == 0:
        print(i)
        result += i
    i += 1
print('0-100之间的偶数累加 = %d' % result)

