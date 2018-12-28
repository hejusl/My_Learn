# !/usr/local/bin/python
# coding=utf-8

# 列表名=[数据1,数据2,数据3,...]
# 列表名=list(可迭代对象)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
student = ['1001', '张三', '16', '海淀']
list2 = list(range(10))

print(list1[5])
print(student)
x = list1[7]

print(x)

# 创建空列表
age = list()

# 列表加法运算
list3 = list1 + list2
print(list3)
# 列表乘法运算
list4 = list1 * 2
print(list4)

# 删除列表中得值
del list1[2]
print(list1)

student.append('d')
print(student)
list1.insert(3, "g")
print(list1)
