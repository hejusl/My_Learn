# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8
# 输入用户年龄
age = int(input('请输入年龄：'))

# 判断是否满 18 岁 >=
if age >= 18:
    # 如果满 18 岁，允许进入网吧嗨皮
    print('你已经成年，欢迎来网吧嗨皮～')

else:
    # 如果未满 18 岁，提示回家写作业
    print('你还没有成年，请回家写作业吧')

