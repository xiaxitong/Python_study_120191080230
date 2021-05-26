#!/usr/bin/env python
#-*-coding:utf-8-*-

#file:do_1.py
#author:HP
#datetime:2021/4/25 20:00
#software: PyCharm
'''
this is function  description 
'''
# import module your need
'''
 编写一个装饰器，能计算其他函数的运行时间；
'''
import time,random

def outer(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print("run time: ",end_time -start_time)
    return inner

@outer  # 相当于 index = outer(index)
def index():
    time.sleep(random.randrange(1,5))
    print("-----it's index time-----")


# index = outer(index)
