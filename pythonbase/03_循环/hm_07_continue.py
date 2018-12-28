# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

i = 0
while i < 10:
    # continue 某一条件满足时，退出循环，不执行后续的重复代码
    if i == 3:
        # 注意，在循环中，如果使用 continue 这个关键字
        # 在使用关键之前需要确认循环的记述4是否修改，
        # 否则可能导致死循环
        i += 1
        continue

    print(i)

    i += 1