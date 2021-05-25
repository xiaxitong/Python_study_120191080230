#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:8-3.py
# author:16546
# datetime:2021/5/19 16:20
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from time import time
from multiprocessing import Pool
def isPrime(n):
    if n<2:
        return 0
    if n in (2,3):
        return 1
    if not n&1:
        return 0
    for i in range(5,int(n**0.5)+1,2):
        #第一个参数即为进程池中进程的数目
        if n%i==0:
            return 0
    return 1
if __name__ =='__main__':
    start = time()
    print(sum(map(isPrime,range(100000))))
    end = time()
    print(end - start)
