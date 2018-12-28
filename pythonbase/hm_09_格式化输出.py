# !/usr/local/Cellar/python3/3.6.3/bin
# coding=utf-8

# 定义字符串变量 name， 输出 我的名字叫 小明，请多关照

name = "小明"
print("我的名字叫: %s ，请多关照！" % name)

# 定义整数变量 student_no, 输出我的学号是 000001
student_mo = 1

print("我的学号是： %a6d" % student_mo)
scale = 0.25
print("数据比例是：%.0f%%" % (scale*100))

# 1 输入苹果的单价
price = float(input('苹果的单价：'))

# 2 输入苹果的重量
weight = float(input('苹果的重量：'))

# 3 计算支付的总金额
money = price * weight
print("苹果的单价: %.2f 元/斤，共买了: %.2f 斤，需要支付: %.2f 元" % (price, weight, money))
