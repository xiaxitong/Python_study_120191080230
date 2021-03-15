#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_args.py
# author:16546
# datetime:2021/3/15 15:45
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def printlist (arg, *vartuple):
    print(arg)
    print(list(vartuple))
def printdic (**vartuple):
    print(vartuple)
if __name__ == '__main__':
    printlist(4,5,8,6,3)
    printdic(a=6,b=8)