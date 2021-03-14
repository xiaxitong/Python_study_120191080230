#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_tup.py
# author:16546
# datetime:2021/3/14 19:50
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == "__main__":
    tup = (78,98,88,68,58)
    tup1 = (78,98,88)
    tup2 = (68,58)
    print(len(tup1))
    tup3 = tup1 + tup2
    tup4 = tup2*2
    print(f'{68 in tup2}')
    for i in tup3:
        print(i)
    for i in tup4:
        print(i)
    print(f'元素个数: {len(tup)}  最大值：{max(tup)} 最小值：{min(tup)}')