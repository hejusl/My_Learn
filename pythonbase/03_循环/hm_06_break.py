# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

i = 0

while i < 10:
    # break 某一条件满足时，退出循环，不再执行后续的重复代码
    if i == 3:
        break
        # continue

    print(i)
    i += 1
print('over')
