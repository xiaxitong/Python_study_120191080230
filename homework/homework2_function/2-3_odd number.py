#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2-3.py
# author:16546
# datetime:2021/4/2 14:50
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
#编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#   数字列表请用随机数函数生成;

import random
def do_list():
    li = []
    li = list(random.randint(0,20) for i in range(10))
    # for i in range(5):
    #     l = random.randint(0,20)
    #     li.append(l)
    for i in li:
        if i%2 !=0:
            print(i)
if __name__ == '__main__':
    do_list()