# !/usr/local/bin/python
# coding=utf-8

# 列表list

# 1.创建列表
# 语法1:列表名=[数据1,数据2,数据3,数据4,...]
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = list(['a', 'b', 'c'])
#语法2:列表名=list(可迭代对象)
list3=list(range(11))
print('%s\n%s\n%s'%(list1,list2,list3))

#2.使用列表
#方法1:通过列表名访问元素
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1)
#方法2:通过列表名加索引访问列表元素
list1=['a','b','c','d']
print(list1[2])
print(list1[-1])
#方法3:通过列表名加索引修改列表元素
list1=['spam', 'Spam', 'SPAM!']
list1[1]='SPam'
print('%s\n%s'%(list1[1],list1))

#3.创建列表说明
#创建空列表
list1=[]
print(list1)
list2=list()
print(list2)
#创建无名列表
[1,2,3]
[]
list((rang(10))
print([1,2,3,'a','b','c'])

#4.列表运算
#列表加法运算
list1=['a','b','c']
list2=[1,2,3]
list3=list1+list2
print(list3)
#列表乘法运算
list1=['1a','2b','3c']
list2=list1*3
print(list2)

#5.嵌套列表
#使用嵌套列表即在列表里创建其它列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
#[['a', 'b', 'c'], [1, 2, 3]]
x[0]
#['a', 'b', 'c']
x[0][1]
#'b'

#6.删除列表
#删除列表元素
list1=[1,2,3,4,5,6,7,8,9,0]
del list1[-1]
print(list1)
#删除列表对象
#del list1

#7.列表常见操作函数
#(1)len() 方法返回列表元素个数
#语法：len(list)
#参数：list -- 要计算元素个数的列表
#返回值：返回列表元素个数
#实例：
list1 = ['Google', 'Runoob', 'Taobao']
print (len(list1))
list2=list(range(5)) # 创建一个 0-4 的列表
print (len(list2))
#输出结果：
#3
#5

#(2)max() 方法返回列表元素中的最大值
#语法：max(list)
#参数：list -- 要返回最大值的列表
#返回值：返回列表元素中的最大值
#实例：
list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
print ("list1 最大元素值 : ", max(list1))
print ("list2 最大元素值 : ", max(list2))
#输出结果：
#list1 最大元素值 :  Taobao
#list2 最大元素值 :  700

#(3)min() 方法返回列表元素中的最小值
#语法：min(list)
#参数：list -- 要返回最小值的列表
#返回值：返回列表元素中的最小值
#实例：
list1, list2 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
print ("list1 最小元素值 : ", min(list1))
print ("list2 最小元素值 : ", min(list2))
#输出结果：
#list1 最小元素值 :  Google
#list2 最小元素值 :  200
sd
#(4)sum() 方法对系列进行求和计算
#语法：sum(iterable[, start])
#参数：iterable -- 可迭代对象，如列表
            start -- 指定相加的参数，如果没有设置这个值，默认为0
#返回值：返回计算结果
#实例：
sum([0,1,2])
sum([0,1,2,3,4], 2)      # 列表计算总和后再加 2
#输出结果：
#3
#12

#8.列表常见操作方法
#(1)append()方法用于在列表末尾追加元素
#语法：list.append(obj)
#参数：obj -- 添加到列表末尾的对象
#返回值：该方法无返回值，但会修改原来的列表
#实例：
list1=[1,2,3,4,5,6,7,8,9]
list1.append(10)
print('Updated List:',list1)
#输出结果：
#Updated List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#(2)insert()方法用于将指定对象插入列表的指定位置
#语法：list.insert(index,obj)
#参数：index -- 对象obj需要插入的索引位置
#          obj ---- 要插入列表中的对象
#返回值：该方法没有返回值，但会在列表指定位置插入对象
#实例：
list1=[1,2,3,4,5,6,7,8,9,10]
list1.insert(0,11)
print('Final List:',list1)
#输出结果：
#Final List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#(3)extend()方法用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
#语法：list.extend(seq)
#参数：seq -- 元素列表
#返回值：该方法没有返回值，但会在已存在的列表中添加新的列表内容
#实例：
list1=[123,'xyz','abc']
list2=[2009,'manni']
list1.extend(list2)
print('Extended List:',list1)
#输出结果：
#Extended List: [123, 'xyz', 'abc', 2009, 'manni']

#(4)pop()方法用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
#语法：list.pop(obj=list[-1])
#参数：obj -- 可选参数，要移除列表元素的对象
#返回值：该方法返回从列表中移除的元素对象
#实例：
list1=[123,'xyz','zara','abc']
print('A List:',list1.pop())
print('B List:',list1.pop(2))
#输出结果：
#A List: abc
#B List: zara

#(5)remove()方法用于移除列表中某个值的第一个匹配项
#语法：list.remove(obj)
#参数：obj -- 列表中要移除的对象
#返回值：该方法没有返回值但是会移除两种中的某个值的第一个匹配项
#实例：
list1=[123,'xyz','zara','abc','xyz']
list1.remove('xyz')
print('List：',list1)
list1.remove('abc')
print('List：',list1)
#输出结果：
#List： [123, 'zara', 'abc', 'xyz']
#List： [123, 'zara', 'xyz']

#(6)clear()方法用于清空列表，类似于del a[:]
#语法：list.clear()
#参数：无
#返回值：该方法没有返回值
#实例：
list1=['Google','Runoob','Taobao','Baidu']
list1.clear()
print('列表清空后：',list1)
#输出结果：
#列表清空后： []

#(7)count()方法用于统计某个元素在列表中出现的次数
#语法：list.count(obj)
#参数：obj -- 列表中统计的对象
#返回值：返回元素在列表中出现的次数
#实例：
list1=[123,'Google','Runoob','Taobao',123]
print('123元素个数：',list1.count(123))
print('Runoob元素个数：',list1.count('Runoob'))
#输出结果：
#123元素个数： 2
#Runoob元素个数： 1

#(8)index()方法用于从列表中找出某个值第一个匹配项的索引位置
#语法：list.index(obj)
#参数：obj -- 查找的对象
#返回值：该方法返回查找对象的索引位置，如果没有找到对象则抛出异常
#实例1：
list1=['Google','Runoob','Taobao']
print('Runoob索引值为',list1.index('Runoob'))
print('Taobao索引值为',list1.index('Taobao'))
#输出结果：
#Runoob索引值为 1
#Taobao索引值为 2
#实例2：
list2=['a','b','c','d','e','f',1,2,3,4,5,6]
print('规定范围内截取"f"的索引：',list2.index('f',0,6))
#输出结果：
#规定范围内截取"f"的索引： 5

#(9)sort() 方法用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数
#语法：list.sort([func])
#参数：func -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序
#返回值：该方法没有返回值，但是会对列表的对象进行排序
#实例：
list1=['Google', 'Runoob', 'Taobao', 'Baidu']
list1.sort()
print ("列表排序后 : ", list1)
#输出结果：
#列表排序后 :  ['Baidu', 'Google', 'Runoob', 'Taobao']

#(10)reverse() 方法用于反向列表中元素
#语法：list.reverse()
#参数：NA
#返回值：该方法没有返回值，但是会对列表的元素进行反向排序
#实例：
list1=['Google', 'Runoob', 'Taobao', 'Baidu']
list1.reverse()
print ("列表反转后: ", list1)
#输出结果：
#列表反转后:  ['Baidu', 'Taobao', 'Runoob', 'Google']

#9.列表推导式
#语法1：[表达式 for 变量 in 序列或可迭代对象]
#实例1：
list1=[1,2,3,4,5]
print([x**2 for x in list1])
print([y for y in range(1,20,2)])
print([z**z for z in range(2,1000,2)])
#输出结果：
#[1, 4, 9, 16, 25]
#[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#[4, 256, 46656, 16777216]
#语法2：[表达式 for 变量 in 列表 if 条件]
#实例2：
list2=[1,2,3,4,5,6,7,8,9]
print([x**2 for x in list1 if x>5])
#输出结果：
#[36, 49, 64, 81]

#10.切片
#语法：[start_index：end_index：step]
#参数1：start_index表示起始索引
#参数2：end_index表示结束索引
#参数3：step表示步长，步长不能为0，且默认值为1
#返回值：切片不会改变原对象，而是重新生成了一个新的对象
#实例1：
list1=['A','B','C','D','E','F']
list1[0:4:1]	#步长为1，获取从索引0开始，到索引4结束但不包含索引4的所有元素
list1[0:4]		#省略step步长，因为步长有默认值为1，因此结果还是一样
#输出结果：
#['A','B','C','D']
#实例2：
list1=['A','B','C','D','E','F']
list1[:5]		#省略start_index，保留end_index，这样会从第一个元素开始，切到end_index-1的元素为止
#输出结果：
#['A','B','C','D','E']
#实例3：
list1=['A','B','C','D','E','F']
list1[2:]		#保留start_index，但省略end_index，这样会从起始索引开始，切到最后一个元素为止
#输出结果：
#['C','D','E','F']
#实例4：
list1=['A','B','C','D','E','F']
list1[:]		#省略start_index、end_index和step，这样就标识切片整个序列，也就是复制出了一个新的序列
#输出结果：
#['A','B','C','D','E','F']
#实例5：
list1=['A','B','C','D','E','F']
list1[::2]		#省略start_index、end_index，但保留step，标识对整个序列，按照步长整除的规则取值：
#输出结果：
#['A','C','E']
#实例6：
list1=['A','B','C','D','E','F']
list1=[::-1]	#如果将步长设为-1，那么久可以得到一个反序的序列了
#输出结果：
#['F','E','D','C','B','A']
#实例7：
list1=['A','B','C','D','E','F']
list1[0:3]		#这四种表达式是等价的
list1[0:-3]
list1[-6:3]
list1[-6:-3]
#输出结果：
['A','B','C']
#实例8：
list1=['A','B','C','D','E','F']
list1[0:3:-1]	#切片时。一定要保证start_index到end_index的方向与步长step的方向同向，否则会切出空的序列
list1[3:0:1]
#输出结果：
#[]