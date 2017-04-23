#coding:utf8

'''
如何对迭代器进行切片操作

问题：
对一个文本文件,我们想读取其中某范围的内容，比如100~300行之间的内容
python中文本文件是可迭代对象，我们是否可以用类似列表切片的方式得到
一个100~300行文件内容的生成器？

方法:
使用标准库中的itertools.islice，他能返回一个迭代对象切片的生成器
'''

from itertools import islice

# 获取10~20行的内容
with open("/var/log/system.log") as f:
    for line in islice(f, 10, 20):
		print line,


# 获取10 到文件末尾的内容
with open("/var/log/system.log") as f:
    for line in islice(f, 10, None):
		print line,
