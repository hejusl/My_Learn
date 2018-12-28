"""
基数
"""
# 先求出0.01元~0.1元的这个档金额的基数，相当于一个最低金额
s_sum = 0
num = 0
i = 0
while i < 10:
    num += 0.01
    num_count = round(num, 2)

    s_sum += num
    result = round(s_sum, 2)

#    if i == 9:
#        print(num_count, '=', end=' ')
#    else:
#        print(num_count, '+', end=' ')

    i += 1

# result表示求出的基数
print(result)
