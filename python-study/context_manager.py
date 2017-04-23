#coding:utf8

'''
如何支持上下文管理

'''

from telnetlib import Telnet
from sys import stdin, stdout
from collections import deque

class Telnet_Client(object):
	def __init__(self, addr, port=23):
		self.addr = addr
		self.port = port
		self.tn = None
	def start(self):
		self.tn = Telnet(self.addr, self.port)
		self.history = deque()
	
		t = self.tn.read_until('login: ')
		stdout.write(t)
		user = stdin.readline()
		self.tn.write(user)

		t = self.tn.read_until("passwd: ")
		if t.startwith(user[:-1]): t = t[len(user) + 1]
		stdout.write(t)
		self.tn.write(stdin.readline())

		t = self.tn.read_until('$ ')
		stdout.write(t)

		while True:
			uinput = stdin.readline()
			if not uniput:
				break
			self.history.append(uinput)
			t = self.tn.read_until('$')
			stdout.write(t[len(uinput) + 1:])

	def cleanu(self):
		self.tn.close()
		self.tn = None
		with open(self.addr + 'history.txt', 'w') as f:
			f.writelines(self.history)

client = Telnet_Client('127.0.0.1')
print '\nstart...'
client.start()
print '\ncleanup'
client.cleanup()
