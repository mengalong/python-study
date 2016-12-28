#coding:utf8

'''
如何在一个for语句中迭代多个可迭代对象

问题：
1. 某班学生期末考试成绩，语文、数学、英语分别存储在3个列表中，
	同时迭代三个列表，计算每个学生的总分(并行)

2. 某年级有4个班，某次考试每班英语成绩分别存储在4个列表中,依次迭代
	每个列表，统计全部学生成绩高于90分的人数(串行)
'''

from random import randint
from itertools import chain

# 问题1:
chinese = [randint(60, 100) for _ in xrange(40)]
math = [randint(60, 100) for _ in xrange(40)]
english = [randint(60, 100) for _ in xrange(40)]

# method 1:
for i in xrange(len(math)):
	chinese[i] + math[i] + english[i]

# 使用内置函数zip，可以将多个可迭代对象合并起来
# 可以尝试 zip([1, 2, 3], ['a', 'b', 'c'])
# 一次循环同时迭代多个可迭代器的内容
total = []
for c, m, e in zip(chinese, math, english):
	total.append(c + m + e)
print total


# 问题2：
# 测试: chain([1, 2, 3, 4], ['a', 'b', 'c'])

e1 = [randint(60, 100) for _ in xrange(40)]
e2 = [randint(60, 100) for _ in xrange(42)]
e3 = [randint(60, 100) for _ in xrange(44)]
e4 = [randint(60, 100) for _ in xrange(34)]

count = 0
for s in chain(e1, e2, e3, e4):
	if s > 90:
		count += 1
print s
