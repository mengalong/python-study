#coding:utf8

'''
如何进行反向迭代以及如何实现反向迭代

问题：
实现一个连续浮点数发生器,根据给定范围和步进值产生一系列
连续浮点数，例如迭代float_range(3.0, 4.0, 0.2)可产生序列:

反向: 4.0 > 3.8 > 3.6 > 3.4 > 3.2 >
正向: 3.0 > 3.2 > 3.4 > 3.6 > 3.8 >

l = [1, 2, 3, 4]
reversed(l) : 实现了对列表的反向，返回可迭代对象
iter(l)：返回正向可迭代对象
'''

class float_range():
	def __init__(self, start, end, step=0.1):
		self.start = start
		self.end = end
		self.step = step

	# 正向迭代器
	def __iter__(self):
		t = self.start
		while t <= self.end:
			yield t
			t += self.step

	# 反向迭代器
	def __reversed__(self):
		t = self.end
		while t >= self.start:
			yield t
			t -= self.step

# float_range(3.0, 4.0, 0.2) 将得到float_range 的 __iter__ 返回的迭代器
# reversed(float_range) 得到的是 __reversed__
print "反向:",
for x in reversed(float_range(3.0, 4.0, 0.2)):
	print x,">",

print 
print "正向:",
for x in float_range(3.0, 4.0, 0.2):
	print x,">",
