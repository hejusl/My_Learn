# /usr/local/bin/python3
# coding=utf-8

file_path = open('/Users/henry/02-Study/01-Python/learning/test.txt', 'w')
num = 1
num_1 = 1
name_last = str(num_1).zfill(5)
while num <= 101:
    file_path.write("'hc_test_user_%s',\n" % name_last)
    num_1 += 1
    name_last = str(num_1).zfill(5)
    num += 1
file_path.close()
