#!/usr/bin/env python
# all buffered
f = open('demo.txt', 'w', buffering=10)
f.write('1' * 10)
f.close()

# line buffered
f = open('demo.txt', 'w', buffering=1)
f.write('abc')
f.write('123')
f.write('\n')
f.close()

# non buffered
f = open('demo.txt', 'w', buffering=0)
f.write('a')
f.write('b')
f.close()
