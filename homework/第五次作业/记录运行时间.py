#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:记录运行时间.py
# author:16546
# datetime:2021/4/27 16:14
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import time,functools
def metric(func):
    def wrapper(*a,**b):
        #wrapper()函数的参数与原函数保持一致，原函数有参就填写上面的两个参数，无参则不填

        start_time = time.time()
        func(*a,**b)
        end_time = time.time()
        print("运行时间为：%s"%(end_time-start_time))
        return func(*a,**b)
        #原函数有返回值时要在wrapper()函数中加上返回值。否则无法输出原函数返回的那个值

    return wrapper

@metric
#@语句自动调用 fast = metric(fast)
#返回的fast 等于wrapper函数，是个全新的函数

def fast(x,y):
    time.sleep(0.0012)
    return x+y
@metric
def slow(x,y,z):
    time.sleep(0.1234)
    return x*y*z

if __name__ == "__main__":
    f = fast(11,22)
    s = slow(11,22,33)
    if f!=33:
        print("测试失败!")
    elif s!=7986:
        print("测试失败!")
    else:
        print("测试成功!")
