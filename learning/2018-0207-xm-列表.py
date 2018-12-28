# !/usr/local/bin/python3
# coding=utf-8
 
# 列表中添加一个新的元素
list_append = []
for i in range(5):
    list_append.append(i)
print('list_append = %s' % list_append)

# 列表末尾一次性追加另一个新列表的多个值
list_extend_1 = ['a', 'b', 'c']
list_extend_2 = ['d', 'e', 'f']
list_extend_1.extend(list_extend_2)
print('list_extend_1 = %s' % list_extend_1)


# 列表中指定对象插入指定位置
list_insert = [1, 2, 3, 4]
list_insert.insert(0, 0)
print('list_insert = %s' % list_insert)


# 移除列表中指定索引位置的元素，如果没有指定索引位置默认移除最后一个
list_pop = ['a', 'b', 'c']
list_pop.pop(1)
print('list_pop = %s' % list_pop)


# 统计某个元素在列表中出现的次数
list_count = ['abc', 'efg', 'hij', 'abc']
print('list_count[0]出现的次数：%s' % list_count.count(list_count[0]))


# 移除列表中某个值的第一个匹配项
list_remove = ['a', 'b', 'c', 'd']
list_remove.remove('d')
print('list_remove = %s' % list_remove)


# 列表中找出某个值第一个匹配项的索引位置
list_index = ['a', 'b', 'c']
print('b在列表中的索引位置：%s' % list_index.index('b'))


# 原列表进行排序
list_sort = ['b', 'a', 'c']
list_sort.sort()
print('list_sort = %s' % list_sort)


# 反向列表元素
list_reverse = ['d', 'e', 'f']
list_reverse.reverse()
print('list_reverse = %s' % list_reverse)


# 清空列表
list_clear = ['光', '明', '正', '大']
list_clear.clear()
print('list_clear = %s' % list_clear)

# 复制列表
list_copy_1 = ['W', 'T', 'F']
list_copy_2 = list_copy_1.copy()
print('list_copy2 = %s' % list_copy_2)
