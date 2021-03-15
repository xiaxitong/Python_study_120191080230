#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_def3.py
# author:16546
# datetime:2021/3/15 14:46
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import random
list1 = [random.randint(0,20) for i in range(10)]
if __name__ == "__main__":
    l = filter(lambda x:x % 2 !=0, list1)
    print(list(l))

