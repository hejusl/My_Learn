# !/usr/local/bin/python3
# coding=utf-8

num = 10
print('Guess what I think?')
answer = input()

result = int(answer) < int(num)
print('too small')
print(result)

result = int(answer) > int(num)
print('too big')
print(result)

result = int(answer) == int(num)
print('equal')
print(result)
