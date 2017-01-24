#coding:utf8
import sys

'''
如何为创建大量实例节省内存

xx游戏中定义了玩家类，Player，每个在线玩家在服务器内存中都有一个
Player实例，当很多人同时在线的时候，将产生大量实例
如何降低这些大量实例的内存开销

解决：
定义累的 __slots_-属性，生命实例属性的列表

'''

class Player(object):
	def __init__(self, uid, name, status=0, level=0):
		self.uid = uid
		self.name = name 
		self.stat = status
		self.level = level

class Player2(object):
	__slots__ = ['uid', 'name', 'stat', 'level']
	def __init__(self, uid, name, status=0, level=0):
		self.uid = uid
		self.name = name 
		self.stat = status
		self.level = level

p1 = Player('001', 'jim')
p2 = Player2('001', 'jim')
# try:
print dir(p1)
print dir(p2)

print set(dir(p1)) - set(dir(p2))

print sys.getsizeof(p1.__dict__) 
#print sys.getsizeof(p2.__dict__)
