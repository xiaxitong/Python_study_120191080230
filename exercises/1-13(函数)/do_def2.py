#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_def2.py
# author:16546
# datetime:2021/3/15 15:41
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
list = [1,2,3,4]
def do_list():
    print(list)
    print(id(list))
    list.append(5)
    print(list)
    print(id(list))
if __name__=="__main__":
    do_list()