#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:递增计数器.py
# author:16546
# datetime:2021/4/18 16:34
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def createCounter():
    x = [0]
    def Counter():
        x[0] = x[0]+1
        return x[0]
    return Counter
#外函数返回的是内函数的函数名，即指向函数的变量，不能加‘（）’

if __name__ == '__main__':
    counterA = createCounter()
    print(counterA(),counterA(),counterA(),counterA(),counterA())
