#coding: utf8

s = "abc"
print s.ljust(10, "=")
print s.rjust(10, "=")
print s.center(10, "=")

print '{:=>10}'.format(s)
print '{:=<10}'.format(s)
print '{:=^10}'.format(s)