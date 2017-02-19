#encoding:utf8
import tarfile
import os
from xml.etree.ElementTree import ElementTree, Element
import csv
from StringIO import  StringIO
import requests
from threading import Thread
from threading import Event


# Queue 是一个线程安全的队列数据结构
from Queue import Queue

'''
实现一个线程，将转换出的xml文件压缩打包，比如转换线程每生产处100个xml文件
就同通知打包线程进行打包，并删除xml文件。打包完成后，打包线程同坐转换线程
转换线程继续转换

线程间的时间通知可以使用 Threading.Event
1. 等待时间一段调用wait，等待事件
2. 通知一端调用set，通知事件
'''



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
    def __init__(self, queue, cEvent, tEvent):
        Thread.__init__(self)
        self.queue = queue
        self.cEvent = cEvent
        self.tEvent = tEvent

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

        count = 0
        while True:
            # 接收线程传递过来的数据 sid, data
            sid, data = self.queue.get()
            print "convert %s" % sid
            if sid == -1:
                self.cEvent.set()
                self.tEvent.wait()
                break
            if data:
                fname = str(sid).rjust(6, '0') + ".xml"
                with open(fname, 'wb') as wf:
                    self.csvToXml(data, wf)
                count += 1
                if count == 5:
                    self.cEvent.set()
                    self.tEvent.wait()
                    self.tEvent.clear()
                    count = 0

class TarThread(Thread):
    def __init__(self, cEvent, tEvent):
        Thread.__init__(self)
        self.count = 0
        self.cEvent = cEvent
        self.tEvent = tEvent
        self.setDaemon(True)

    def tarXML(self):
        self.count += 1
        tfname = '%d.tgz' % self.count
        tf = tarfile.open(tfname, 'w:gz')
        for fname in os.listdir('.'):
            if fname.endswith(".xml"):
                tf.add(fname)
                os.remove(fname)
        tf.close()

        if not tf.members:
            os.remove(tf)

        print "create tar %s" % self.count

    def run(self):
        while True:
            self.cEvent.wait()
            self.tarXML()
            self.cEvent.clear()
            self.tEvent.set()



if __name__ == "__main__":
    q = Queue()
    dThreads = [DownloadThread(i, q) for i in xrange(1, 11)]

    cEvent = Event()
    tEvent = Event()

    cThread = ConvertThread(q, cEvent, tEvent)

    tThread = TarThread(cEvent, tEvent)
    tThread.start()

    for t in dThreads:
        t.start()

    cThread.start()

    for t in dThreads:
        t.join()

q.put((-1, None)) #通知退出