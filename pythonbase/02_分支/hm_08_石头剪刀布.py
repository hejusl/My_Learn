# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8
# 从控制台输入要出的拳 - - - 石头（1），剪刀（2），布（3）
# 电脑随机出拳 - - 先假定电脑只会出石头，完成整体代码功能
# 比较胜负

import random


while 1:
    player = input('请玩家出拳,石头，剪刀，布：')
    if player == '石头' or player == '剪刀' or player == '布':
        if player == '石头':
            p1 = 1
        elif player == '剪刀':
            p1 = 2
        elif player == '布':
            p1 = 3
        break
    else:
        print('出拳错误,请重新出拳')

computer = random.randint(1, 3)
if computer == 1:
    c1 = '石头'
elif computer == 2:
    c1 = '剪刀'
else:
    c1 = '布'
print('玩家选择的拳是： %s - 电脑出的拳是：%s' % (player, c1))

# 比较胜负
# 石头 胜 剪刀
# 剪刀 胜 布
# 布 胜 石头

if ((p1 == 1 and computer == 2)
        or (p1 == 2 and computer == 3)
        or (p1 == 3 and computer == 1)):
    print('玩家胜利！')
# 平局
elif p1 == computer:
    print('真是心有灵犀，再来一盘')

# 其他情况就是电脑获胜
else:
    print('不服气，我们决战到天明！')
