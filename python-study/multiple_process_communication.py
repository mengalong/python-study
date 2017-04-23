#encoding:utf8
from xml.etree.ElementTree import ElementTree, Element
import csv
from StringIO import  StringIO
import requests
from threading import Thread

# Queue 是一个线程安全的队列数据结构
from Queue import Queue

def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level



class DownloadThread(Thread):
    def __init__(self, sid, queue):
        Thread.__init__(self)
        self.sid = sid
        self.url = 'http://table.finance.yahoo.com/table.csv?s=%s.sz'
        self.url %= str(sid).rjust(6, '0')
        self.queue = queue

    def download(self, url):
        response = requests.get(url, timeout=3)
        if response.ok:
            return StringIO(response.content)

    def run(self):
        print "download :%s \n" % self.sid
        # download the url
        data = self.download(self.url)

        # transfer the data to convert process
        # lock
        self.queue.put((self.sid, data))

class ConvertThread(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def csvToXml(self, scsv, fxml):
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

    def run(self):

        while True:
            # 接收线程传递过来的数据 sid, data
            sid, data = self.queue.get()
            print "convert %s" % sid
            if sid == -1:
                break
            if data:
                fname = str(sid).rjust(6, '0') + ".xml"
                with open(fname, 'wb') as wf:
                    self.csvToXml(data, wf)

q = Queue()
dThreads = [DownloadThread(i, q) for i in xrange(1, 3)]
cThread = ConvertThread(q)

for t in dThreads:
    t.start()

cThread.start()

for t in dThreads:
    t.join()

q.put((-1, None)) #通知退出

