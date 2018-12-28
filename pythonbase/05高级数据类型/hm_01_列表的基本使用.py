# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

name_list = ["zhangshan", 'lisi', 'wangwu']

# 1、取值和索引
# llist index out of range - 列表索引超出范围
print(name_list[2])

# 知道数据的内容，想确定数据在列表中的位置
# 使用index方法注意：如果传递的数据不在列表中程序会报错
print(name_list.index('wangwu'))

# 2 修改
name_list[1] = '李四'

# list assignment index out of range
# 列表指定的索引超出范围，程序报错
# name_list[3] = '王小二'
# 3 增加
# append方法可以向列表中追加数据
name_list.append("王小二")
# insert 方法可以在列表指定索引位置 插入数据
name_list.insert(1, "小美眉")
# extend 方法可以把其他列表的完整内容，追加到列表末尾
tem_list = ["孙悟空", "祝二哥", "沙师弟"]
name_list.extend(tem_list)
# 4 删除
# remove 可以从列表中删除指定数据
name_list.remove('wangwu')
# pop 方法默认把列表最后一个元素删除
name_list.pop()
# pop 方法可以删除指定元素的索引
name_list.pop(3)
# clear 方法可以清空列表
name_list.clear()
print(name_list)

