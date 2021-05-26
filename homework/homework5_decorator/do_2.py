#!/usr/bin/env python
#-*-coding:utf-8-*-

#file:do_2.py
#author:HP
#datetime:2021/4/25 20:03
#software: PyCharm
'''
this is function  description 
'''
# import module your need
'''
 编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中
'''
import os,time
def outer(func):
    def inner():
        d =time.asctime()
        print(d)
        f = open(r'D:\python\Python_study_exercise\test.txt','w',encoding='gbk')
        f.write(d)
        f.close()
        func()
    return inner

@outer
def index():
    pass

index()
