# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

name_list = ['张三', '李四', '王五']

del name_list[1]
# （知道）使用 del 关键字 删除列表元素

# del 的本质是用来将一个变量从内存中删除
name = '小明'

del name

# 注意：如果使用 del 关键字将变量从内存中删除
# 后续的代码就不能再使用这个变量

print(name)
print(name_list)