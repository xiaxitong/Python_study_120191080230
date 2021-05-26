#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:记录运行日志.py
# author:16546
# datetime:2021/4/27 16:15
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
# 编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；
from datetime import datetime
filename = 'log.txt'
def timmer(func):
    def wrapper(*a,**b):
        with open(filename, 'w', encoding='utf-8') as f:
            t = datetime.now().date()
            f.write(f'运行日期为：{t}\n')
            f.write(f'运行函数为：{func.__name__}\n')
        return func(*a,**b)
    return wrapper
@timmer
def Add(x,y):
    return x+y

if __name__ == "__main__":
    a = Add(11,33)
    with open( filename,'a',encoding='utf-8') as f:
    #'w'模式会重写文档
    #'a'是追加模式，在文档末尾添加数据

        f.write(f'运行结果为：{a}')