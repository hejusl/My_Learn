# !/usr/local/bin/python3
# coding=utf-8

###########################
'''
print('Who do you think I am')
you = input()
print('Oh, yes!')
print(you)
a = 1<3
print (not a)
b = 1
c = 3
#
print(b > c)

num = 10
print ('Guess what I think?')
answer = int(input())
#
if answer < num:
    print('too small!')
if answer == num:
    print('BINGO!')
if answer > num:
    print('too big!')
print(math.pi)
'''
#############################
#############################
'''
num = 10
print('Guess what I think?')
#
bingo = False
#
while bingo == False:
    answer = int(input())
    if answer < num:
         print('too small!')
    if answer == num:
         print('BINGO!')
         bingo = True
    if answer > num:
         print('too big!')

'''
##############################
##############################
'''
##############################
num = 10
print('Guess what I think?')
#
bingo = False
#
while bingo == False:
    answer = int(input())
    if answer < num:
         print('too small!')
    if answer == num:
         print('BINGO!')
         bingo = True
    if answer > num:
         print('too big!')
'''
##############################
##############################
'''
from random import randint
#
num = randint(1,100)
print('Guess what I think?')
bingo = False
#
while bingo == False:
    answer = int(input())
    if answer < num:
         print('too small!')
    if answer == num:
         print('BINGO!')
         bingo = True
    if answer > num:
         print('too big!')

'''
##############################
##############################
'''
i = 1
s = 0
while i <= 1000:
    s += i
    i += 1
print(s)
'''
##############################
##############################
'''

s = 0
for i in range(1,101):
    s += i
print(s)
str = "'He said, "I'm yours!""
print(str)
str1 = "\\\_v_//"
print(str1)

'''
##############################
##############################
'''

str1 = 'good'
str2 = 'bye'
print("very" + str1)
print(str1 + 'and' + str2)
num = 18
print('My age is ' + str(num))
print('My age is %d' % num)

'''
##############################
##############################
'''

for i in range(0,5):
    for j in range(0,5):
        print('*',end='')
    print()

'''
##############################
##############################
'''

for i in range(0,5):
    for j in range(0,i+1):
        print('*',end='')
    print()

'''
##############################
##############################
'''

print('bool(0) = %s' % bool(0))
#
print('bool('') = %s' % bool(''))
#
print('bool("") = %s' % bool(""))
#
print('bool(None) = %s' % bool(None))

'''
##############################
##############################
'''

def sayHello(someone):
    print (someone + 'Hello World!')

sayHello('we ')

'''
##############################
##############################
'''

def plus(num1,num2):
    print(num1+num2)
#
x = int(input("x= "))
y = int(input("y= "))
print('x+y= ',end='')
plus(x,y)

'''
##############################
##############################
'''
from random import randint


def isEqual(num1, num2):
    if num1 < num2:
        print('Too small')
        return False;
    if num1 > num2:
        print('Too big')
        return False;
    if num1 == num2:
        print('BINGO!')
        return True;


num = randint(1,100)
print('Guess what I think?')
bingo = False
while bingo == False:
    answer = int(input())
    if answer < 0:
        print('Exit game...')
    break
    bingo = isEqual(answer, num)
'''

##############################
##############################
'''

a = 3
if a == 1:
    print('right')
else:
    print('wrong')

'''
##############################
##############################
'''

if a == 1:
    print('one')
elif a ==2:
    print('two')
else:
    print('other')

'''
##############################
##############################
'''

if a == 1:
    print('one')
elif a == 2:
    print('two')
elif a == 3:
    print('three')
else:
    print('too many')

'''
##############################
##############################
'''

def isEqual(num1,num2):
    if num1 < num2:
        print('too small')
        return False;
    elif num1 > unm2:
        print('too big')
        return False;
    else:
        print('BINGO!')
        return True

'''
##############################
##############################
'''

x = int(input())
y = int(input())
#
if x>= 0:
    if y >= 0:
        print('1')
    else:
        print('4')
else:
    if y < 0:
        print('3')
    else:
        print('2')

'''
##############################
##############################
'''
for i in range(1,10):
    print(i,end='')
I = [365, 'everyday', 0.618, True]
print(I[0])
I[0]=123
print(I)
#
I.append(1024)
print(I)
print(I[0:3])
print(I[:3])
print(I[1:])
print(I[:])
'''
##############################
##############################
'''


'''## 点球小游戏  ##

'''
from random import choice
score_you = 0
score_com = 0
direction = ['left', 'center', 'right']

for i in range(5):
    print('====Round %d - You Kick! ===='%(i+1))
    print('Choose one side to shoot:')
    print('left, center, right')
    you = input()
    print('You kicked ' + you)
    com = choice(direction)
    print('Computer saved ' + com)
    if you != com:
        print('Goal!')
        score_you += 1
    else:
        print('Oops...')

    print('Score: %d(you) - %d(com)\n' %(score_you, score_com))

'''
##############################
##############################
'''
# *--字符串分割--*
sentence = "I'm an English sentence"
t = sentence.split()
print(t)

section = "Hi. I am the one. Bye."
s = section.split('.')
print(s)

'''
##############################
##############################
'''
from random import  choice

choice

score = [0, 0]
direction = ['left', 'center', 'right']


def kick():
    print('====You Kick!====')
    print('Choose one side to shoot: ')
    print('left', 'center', 'right')
    you = input()
    print('You kicked ' + you)
    com = choice(direction)
    print('Computer saved ' + com)
    if you !=com:
        print('Goal!')
        score[0] +=1
    else:
        print('Oops...')

    print('Score: %d(you) - %d(com)\n' %(score[0],score[1]))

    print('====You Save!====')
    print('Choose one side to save: ')
    print('left', 'center', 'right')
    you = input()
    print('You saved ' + you)
    com = choice(direction)
    print('Computer kicked ' + com)
    if you ==com:
        print('Saved')
    else:
        print('Oops')
        score[1] +=1
    print('Score: %d(you) - %d(com)\n' % (score[0], score[1]))

for i in range(5):
    print('==== Round %d ====' %(i+1))
    kick()

while(score[0] == score[1]):
    i += 1
    print('==== Round %d ====' %(i+1))
    kick()
if score[0] > score[1]:
    print('You Win!')
else:
    print('You Lose.')


'''
##############################
##############################

# --字符串连接--
'''
s = ';'
li = ['apple', 'pear', 'orange']
fruit = s.join(li)
print(fruit)
print(li)
'''

##############################
##############################
'''
word = 'hello world'
for x in word:
    print(x)

newword = ','.join(word)
print(newword)

f = open('data.txt')
data = f.read()
print(data)
print('***')

data = f.readline(2)
print(data)
print('***')
data = f.readlines()
print(data)
print('***')
f.close()

data = 'I will be in a file.\nSO cool! again\n'
out = open('data.txt', 'a')
out.write(data)
out.close()
'''
##############################
##############################
'''
f = open('/Users/henry/02-Study/01-Python/learning/scores.txt')
lines = f.readlines()
f.close()
print('lines', lines)
results = []
for line in lines:
    print('line', line)
    data = line.split()
    print('data', data)
    sum1 = 0
    for score in data[1:]:
        sum1 += int(score)
    result = '%s\t %d\n' % (data[0], sum1)
    print('result', result)
    results.append(result)
print('results', results)
output = open('result.txt', 'w')
output.writelines(results)
output.close()
'''
##############################
##############################
'''
while True:
    a = input()
    if a == 'FH':
        break
'''
'''
for i in range(10):
    b = input()
    if b == 'fh':
        break
'''

##############################
##############################
'''
i = 0
while i < 5:
    i += 1
    for j in range(3):
        print(j)
        if j == 2:
            break
    for k in range(3):
        if k == 2:
            continue
        print(k)
    if i > 3:
        break
    print(i)
'''



##############################
##############################
'''
sum = 0
data = [12, 34, 68, 61, 59, 80]
for s in data[0:]:
    point = int(s)
    if point < 60:
        continue
    sum += point
print(sum)

'''

##############################
##############################

'''
# noinspection PyBroadException
try:
    f = open('data.txt')
    print('File opened!')
    f.close()
except:
    print("File not exist.")
print('Done')
'''
##############################
##############################
import random
from math import pi as my_pi

d = {'key1': 'value1', 'key2': 'value2'}
print(d['key1'])
score = {'萧峰': 95, '段誉': 97, '虚竹': 89}
print(score['段誉'])
for name in score:
    print(score[name])
score['虚竹'] = 91
score['慕容复'] = 88
del score['萧峰']

for name in score:
    print(name, score[name])
print(random.randint(1, 3))
print(random.choice([1, 3, 5]))
print(my_pi)

##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################
##############################
'''



'''
##############################

