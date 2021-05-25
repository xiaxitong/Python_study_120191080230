#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:h_1_5.py
# author:16546
# datetime:2021/3/23 16:41
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import random
if __name__ == '__main__':
    a = list (range(1,10))
    print(a)
    l = random.sample(a,5)
    print(l)
    b = tuple(range(1,10))
    print(b)
    d = tuple(random.sample(b,5))
    print(d)