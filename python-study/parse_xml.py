# encoding=utf8
from xml.etree.ElementTree import parse

f = open('demo.xml')
et = parse(f)
root = et.getroot()

print root.attrib
print root.text
print root.getchildren()

for child in root:
    print child.get('id')   # get the attrib

print root.find('book')
print root.findall('book')

for e in root.iterfind('book'):
    print e.get('id')

print list(root.iter())
print list(root.iter('title'))

print root.findall('book/*')

print root.findall('.//title')      #递归查询所有的title标签
print root.findall(".//title/..")   #查找title的父节点

print root.findall('book[@id="1"]') #查找指定标签&指定属性
print root.findall('book[price="20"]') #查找指定标签 & 指定tag的值
