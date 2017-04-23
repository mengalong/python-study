#encoding:utf8
from xml.etree.ElementTree import ElementTree, Element
import csv
from StringIO import  StringIO
import requests
from threading import Thread

def download(url):
    response = requests.get(url, timeout=3)
    if response.ok:
        return StringIO(response.content)

def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level

def csvToXml(scsv, fxml):
    reader = csv.reader(scsv)
    headers = reader.next()
    headers = map(lambda h: h.replace(' ', ''), headers)

    root = Element('Data')
    for row in reader:
        e_row = Element('Row')
        root.append(e_row)

        for tag, text in zip(headers, row):
            e = Element(tag)
            e.text = text
            e_row.append(e)
    pretty(root)
    et = ElementTree(root)
    et.write(fxml)


def handle(sid):
    print 'Download...(%d)' % sid
    url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
    url %= str(sid).rjust(6, '0')
    rf = download(url)
    if rf is None: return
    print 'Convert to Xml...(%d)' % sid
    fname = str(sid).rjust(6, '0') + ".xml"
    with open(fname, 'wb') as wf:
        csvToXml(rf, wf)

''' 方法一
t = Thread(target=handle, args=(1,))
t.start()
'''

class MyThread(Thread):
    def __init__(self, sid):
        Thread.__init__(self)
        self.sid = sid

    def run(self):
        handle(self.sid)

threads = []
for i in xrange(1, 3):
    t = MyThread(i)
    threads.append(t)
    t.start()

for t in threads:
    t.join()    #等待子线程退出

print "main thread"

# python 中的多线程只适合并发处理IO型的操作, 不适合并发处理CPU密集型任务
# 因为python有一个全局解释器锁：global interpreter lock
# https://docs.python.org/2.7/c-api/init.html#thread-state-and-the-global-interpreter-lock
# https://docs.python.org/2.7/glossary.html?highlight=glossary#term-global-interpreter-lock