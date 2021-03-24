#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:h_1_7.py
# author:16546
# datetime:2021/3/24 15:58
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == '__main__':
    for i in range(1,10):
        for j in range(1,i+1):
            print(f'{j}*{i}={j*i}',end = '\t')
        print('\n')