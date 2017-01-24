#coding: utf8
import re


'''
we need split a string by mutiple seprator
such as:
InPut: string = "ab,cd|ef;gh\topq,xyz,,aa"
OutPut: ['ab', 'cd', 'ef', 'gh', 'opq', 'xyz', 'aa']
'''

def parser_the_string_by_split(string=None, ds=None):
    res = [string]

    for d in ds:
        t = []
        map(lambda x: t.extend(x.split(d)), res)
        res = t
    return [x for x in res if x]

def parser_the_string_by_re_split(string=None, ds=None):
    res = re.split(ds, string)
    return [x for x in res if x]


if __name__ == "__main__":
    string = "ab,cd|ef;gh\topq,xyz,,aa"
    seprator = "[,;|\t]"

    print parser_the_string_by_split(string, seprator)
    print parser_the_string_by_re_split(string, seprator)