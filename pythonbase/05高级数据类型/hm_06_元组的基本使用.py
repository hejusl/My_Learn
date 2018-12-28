# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

info_tuple = ('zhangsan', 18, 1.75, 'zhangsan')
name_list = ['zhangsan', 'lisi', 'wangwu', 'wangxiaoer']
# 1. 取值和索引
print(info_tuple[0])
# 已经知道数据内容，希望知道该数据在元组中的索引
print(info_tuple.index('zhangsan'))
print(name_list.index('zhangsan'))

# 2. 统计计数
print(info_tuple.count('zhangsan'))
print(name_list.count('zhangsan'))
# 统计元组中包含元素个数
print(len(info_tuple))
print(len(name_list))

