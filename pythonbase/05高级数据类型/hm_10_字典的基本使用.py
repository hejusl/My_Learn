# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

xiaoming_dict = {"name": "小明"}

# 1. 取值
print(xiaoming_dict["name"])
# 在取值的时候，如果指定的 key 值不存在，程序会报错
# print(xiaoming_dict["name123"])

# 2. 增加/修改
# 如果 key 不存在，会新增键值对，如果存在，会修改键值对
xiaoming_dict["age"] = 18
xiaoming_dict["name"] = '小小明'

# 3. 删除
# xiaoming_dict.pop("age")

print(xiaoming_dict)