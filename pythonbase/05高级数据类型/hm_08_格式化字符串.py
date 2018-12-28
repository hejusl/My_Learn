# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

# 格式化字符串后面 （）本质上就是元组

info_tuple = ('小明', 18, 1.75)
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple

print(info_str)
