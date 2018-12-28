# !/usr/local/bin/python3.6
# coding=utf-8

#  字符串
str1 = "this is string example....wow!!!"
str2 = "exam"

print('str1 =', str1)
print('str2 =', str2)
# 序列操作
print('===序列操作===')
print('str1的长度: len(str1) = ', len(str1))  # 字符串str1长度, len()
print('str2的长度: len(str2) = ', len(str2))  # 字符串str2长度, len()
print('str1的第一个字符: str1[0] = ', str1[0])  # str1的第一个字符，索引0的位置
print('str1的最后一个字符: str1[-1] = ', str1[-1])  # str1的最后一个字符，可以用-1表示
print('str1的分片从索引1到索引2: str1[1:3] = ', str1[1:3])

#  find
print('从str1的下标0开始，查找str2中第一个出现的字符位置：str1.find(str2) =', str1.find(str2))  # 从下标0开始，查找str2第一个出现的字符位置，15
print('从下标10开始，查找str2，str1.find(str2, 10)=', str1.find(str2, 10))  # 从下标10开始，查找str2
print('str1.find(str2, 40)=', str1.find(str2, 40))  # 从下标40开始，查找str2
print("str1.replace(str2, '2w2')", str1.replace(str2, '2w2'))  # 用2w2替换str1
print('打印str1 =', str1)

line = 'aaa, bbb, cccc, dd\n'
print(line)
print(line.split( ))


