#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_list_3.py
# author:16546
# datetime:2021/3/14 19:29
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == "__main__":
    list = [80, 90, 98, 78, 58]
    list.sort()
    for i in list:
        print(i)
    list.insert(2,68)
    print("\n")
    for i in list:
        print(i)