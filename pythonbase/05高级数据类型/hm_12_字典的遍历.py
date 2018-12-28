# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

xiaoming_dict = {"name": "小明",
                 "qq": "123456",
                 "phone": "10086"}

# 迭代遍历字典
# 变量 k 是每一次循环中，获取到的键值对的key

for k in xiaoming_dict:

    print("%s - %s" % (k, xiaoming_dict[k]))
