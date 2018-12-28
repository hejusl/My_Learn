# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8
# 1. 定义布尔变量 has_ticket 表示是否有车票
# 2. 定义整型变量 knife_length 表示刀的长度，单位：厘米
# 3. 首先检查是否有车票，如果有，才允许安检
# 4. 安检时，需要检查刀的长度，判断是否超过20厘米
# 5. 如果没有车票不允许进门
has_ticket = True
knife_length = 30
if has_ticket:
    print('车票检查通过，开始安检')
    if knife_length <= 20:
        print('安检通过，可以上车，祝您路途愉快')
    else:
        print("安检失败，您携带的刀太长了，有 %d 厘米长" % knife_length)

else:
    print('请首先买票')