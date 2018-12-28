# 计算投注注数
from itertools import combinations


def bet_number(count, how_num):
    a = []
    for m in range(count):
        a.append(m)

    b = list(combinations(a, how_num))
    # print(b)

    num = 0
    for n in b:
        num += 1
    print(num)

# bet_number(11, 3)

for n in range(2, 12):
    print('选择', n, end='个投注号码，投注注数：')
    bet_number(n, 4)