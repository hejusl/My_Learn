# !/usr/local/bin/python3
# coding=utf-8

# 定义列表list1
list1 = ['Google', 1997, 'woniuxy', 2000]
print("list1列表是%s" % (list1))
print("list1[0:1]代表,从索引0到索引1之前的值%s" % (list1[0:1]))
print("list1[1:3]代表,从索引1到索引3之前的值%s" % (list1[1:3]))
print("list1[-2]代表,列表中倒数第二个值%s" % (list1[-2]))
print("list1[1:]代表,从索引1到索引末尾的值%s" % (list1[1:]))
print("list1[5:]代表,从索引5到索引1之前的值%s" % (list1[5:]))
# 列表的值更新
list1[3] = '2016'
print(list1)

list2 = [1, 2, 3, 4]
list3 = list1+list2
# 列表连接
print(list1+list2)
print(list1+list2[3:])
print(list3)
del list3[3]
print(list3)
