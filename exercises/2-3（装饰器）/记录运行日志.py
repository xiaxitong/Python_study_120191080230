#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:记录运行日志.py
# author:16546
# datetime:2021/4/27 15:40
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from datetime import datetime
def timmer(func):
    def wrapper(*a,**b):
        t = datetime.now().date()
        print(f'运行日期为：{t}')
        print(f'运行函数为：{func.__name__}')
        return func(*a,**b)
    return wrapper
@timmer
def Add(x,y):
    return x+y

if __name__ == "__main__":
    a = Add(11,33)
    print(f'运行结果为：{a}')
















