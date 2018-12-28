# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

hello_str = "hello world"

# 1 判断是否以指定字符串开始
print(hello_str.startswith("hello"))


# 2 判断是否以指定字符串结束
print(hello_str.endswith("world"))


# 3 查找指定字符串
#   index 同样可以查找指定的z字符串在大字符串中的索引
print(hello_str.find("llo"))
#   index 方法，如果指定的字符串不存在，程序会报错
#   find 方法，如果指定的字符串不存在，会返回 -1
print(hello_str.find("abc"))

# 4 替换字符串
#   replace 方法执行完成后，会返回一个新的字符串
#   注意：不会修改原有字符串的内容
print(hello_str.replace("h", "H"))
print(hello_str.replace("world", "python"))
tepm = hello_str.replace("world", "PPP")
print(tepm)
print(hello_str)
