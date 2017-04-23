#coding=utf8

import re

"""
convert the string format:

Input:
str_arr = ["2017-01-24 11:11:11 tttt",
           "2017-01-23 12:12:12 xxxx",
            ]
OutPut:
['01/23/2017 12:12:12 xxxx', '01/23/2017 12:12:12 xxxx']
"""

str_arr = ["2017-01-24 11:11:11 tttt",
           "2017-01-23 12:12:12 xxxx",
            ]

print [ re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', str_arr[1]) for x in str_arr]
print [ re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', str_arr[1]) for x in str_arr]