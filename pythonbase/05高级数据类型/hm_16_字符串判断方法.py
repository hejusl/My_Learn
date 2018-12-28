# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

# 1 判断空白字符，包括 制表符、换行、回车
space_str = "   \t\n\r"

print(space_str.isspace())

# 2 判断字符串中，是否只包含 数字
#   都不能判断小数;
#   num_str = "1.1"
#   unicode字符串
#   num_str = "\u00b2"
#   中文数字
#   num_str = "一千零一"
num_str = ""
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())


# isdigit()
# True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
# False: 汉字数字
# Error: 无
#
# isdecimal()
# True: Unicode数字，，全角数字（双字节）
# False: 罗马数字，汉字数字
# Error: byte数字（单字节）
#
# isnumeric()
# True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
# False: 无
# Error: byte数字（单字节）
# ---------------------
# 作者：lm_y
# 来源：CSDN
# 原文：https://blog.csdn.net/Com_ma/article/details/77539833
# 版权声明：本文为博主原创文章，转载请附上博文链接！