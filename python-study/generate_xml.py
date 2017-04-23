from xml.etree.ElementTree import ElementTree, Element
import csv
from StringIO import  StringIO
import requests

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

if __name__ == "__main__":
    url = 'http://table.finance.yahoo.com/table.csv?s=000001.sz'
    rf = download(url)
    if rf:
        with open('0000001.xml', 'wb') as wf:
            csvToXml(rf, wf)
