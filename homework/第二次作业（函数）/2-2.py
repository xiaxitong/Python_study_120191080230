#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2-2.py
# author:16546
# datetime:2021/4/2 14:50
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def do_sum():
    sum = 0
    n = int(input("接收n个数字："))
    for i in range(0,n):
        if i < n :
            x = int(input("输入数字："))
            sum = sum + x
        else :
            break
    print(sum)
if __name__ == '__main__':
    do_sum()