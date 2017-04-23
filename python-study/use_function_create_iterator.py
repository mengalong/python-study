#coding:utf8

'''
实现一个可迭代对象的类,他可以迭代出给定范围内的所有素数
将该类的__iter__方法实现成生成器函数,每次yield一个素数

这种方案省去了实现可迭代对象,不用实现具体的next()方法
'''

class prime_numbers():
	def __init__(self, start, end):
		self.start = start
		self.end = end
	
	# 判断是否为素数
	def is_prime_num(self, k):
		if k < 2:
			return False
		for i in xrange(2, k):
			if k % i == 0:
				return False
		return True

	def __iter__(self):
		for k in xrange(self.start, self.end + 1):
			if self.is_prime_num(k):
				yield k

for x in prime_numbers(1, 100):
	print x

