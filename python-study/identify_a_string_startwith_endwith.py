#coding: utf8
import os
import stat

"""
modify all the *.py and *.sh permission, add it +x
use str.startwith() and str.endwith()
"""

all_the_file = os.listdir('.')

for filename in all_the_file:
    if filename.endswith((".sh", ".py")):
        os.chmod(filename, os.stat(filename).st_mode | stat.S_IXUSR)
        print oct(os.stat(filename).st_mode)
