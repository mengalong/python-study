from xml.etree.ElementTree import ElementTree, Element
import csv

def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child, level + 1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level

def csvToXml(fname):
    with open(fname, 'rb') as f:
        reader = csv.reader(f)
        headers = reader.next()

        root = Element('Data')
        for row in reader:
            e_row = Element('Row')
            root.append(e_row)

            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                e_row.append(e)
    pretty(root)
    return ElementTree(root)

et = csvToXml('pingan.csv')
et.write('pingan.xml')