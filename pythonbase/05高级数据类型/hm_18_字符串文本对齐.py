# !/usr/local/Cellar/python3/3.6/bin
# coding=utf-8


# 要求：按顺序，并且剧中对齐输出以下内容：
poem = ["\t\n登黄鹤楼",
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:

    # 显示用Strip方法去除字符串中的空白字符
    # 再使用Center方法剧中字符串

    print("|%s|" % (poem_str.strip().center(10, "　")))
