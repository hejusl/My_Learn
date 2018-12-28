"""
奖金分配方案
"""

# from decimal import *

# 保留金额小数点2位
rate_01 = 0.01 / 3
# 每日红包金额30%占每日红包总金额的比例
rate_30 = 0.29 + rate_01
# 每日红包金额30%占每日红包总金额的比例
rate_40 = 0.41 + rate_01
# 实际每日红包金额100占每日红包总金额的比例
rate_total = 0.999999


"""
# 比例原理
num_1 = 29 + 41 + 29
print(num_1)

num_2 = 1 / 3
print(num_2)

num_3 = num_2 * 3
print(num_3)
"""


# 每日红包总数
count_total = 450
# 每日红包总数80%的数量 = 每日红包总数 * 每日红包总数的80%
day_count_a = count_total * 0.8
# 每日红包金额30%的金额 = 每日红包总数80%的数量 * 每日红包金额30%的一轮基数（0.55） / 10
day_money_a = day_count_a * 0.55 / 10
# print(day_money_a)
# 每日红包总金额 = 每日红包金额30%的金额
money_total = day_money_a / rate_30


# print('每日红包总数：' + str(count_total) + '   ' + '每日红包总金额：' + str(money_total))


# 每日红包金额40%的金额
day_money_b = money_total * rate_40
# print(day_money_b)

# 每日红包金额30%的金额（1元~5元）
day_money_c = money_total * rate_30
# print(day_money_c)


# 每日红包总数18%的数量
day_count_b = count_total * 0.18
# print(day_count_b)

# 每日红包总数02%的数量
day_count_c = count_total * 0.02
# print(day_count_c)

if day_count_a.is_integer() and day_count_b.is_integer() and day_count_c.is_integer():

    if 0.1 < day_money_b and 1 < day_money_c:
        print('每日红包总数：' + str(count_total))
        print('每日红包总金额：' + str(money_total))
        print('------------------------------------------------------------')
        print('每日红包总数的80%(0.01元~0.10元),数量：' + str(day_count_a))
        print('每日红包总数的18%(0.10元~1.00元),数量：' + str(day_count_b))
        print('每日红包总数的02%(1.00元~5.00元),数量：' + str(day_count_c))
        print('------------------------------------------------------------')
        print('每日红包金额的30%(0.01元~0.10元)，金额：' + str(day_money_a))
        print('每日红包金额的40%(0.10元~1.00元)，金额：' + str(day_money_b))
        print('每日红包金额的30%(1.00元~5.00元)，金额：' + str(day_money_c))

    """
    # 验证每日红包总数的80%为0.01元~0.1元，该奖级范围的每日红包金额占每日红包总金额的30%
    
    # 金额0.01元，个数占总数比例10%
    day_count_a_001 = count_total * 0.1
    # 金额0.02元，个数占总数比例10%
    day_count_a_002 = count_total * 0.1
    # 金额0.03元，个数占总数比例5%
    day_count_a_003 = count_total * 0.05
    # 金额0.04元，个数占总数比例5%
    day_count_a_004 = count_total * 0.05
    # 金额0.05元，个数占总数比例10%
    day_count_a_005 = count_total * 0.1
    # 金额0.06元，个数占总数比例5%
    day_count_a_006 = count_total * 0.05
    # 金额0.07元，个数占总数比例5%
    day_count_a_007 = count_total * 0.05
    # 金额0.08元，个数占总数比例10%
    day_count_a_008 = count_total * 0.1
    # 金额0.09元，个数占总数比例10%
    day_count_a_009 = count_total * 0.1
    # 金额0.10元，个数占总数比例10%
    day_count_a_010 = count_total * 0.1
    
    # 计算
    day_count_a_total = day_count_a_001 + day_count_a_002 + day_count_a_003 + day_count_a_004 + day_count_a_005 + \
                        day_count_a_006 + day_count_a_007 + day_count_a_008 + day_count_a_009 + day_count_a_010
    
    if day_count_a_total == day_count_a:
        print('验证通过')
    """