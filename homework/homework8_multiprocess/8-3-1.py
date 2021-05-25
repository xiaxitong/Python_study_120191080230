#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:8-3-1.py
# author:16546
# datetime:2021/5/19 16:35
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from time import time
def maan(n,m):
    count = 0
    # 遍历n-m（含nm）间的所有数字并赋值给i
    for i in range(n, m + 1):
        # 遍历2-i中的数并赋值给x
        for x in range(2, i):
            # 判断i能否被j取整，能取整说明能被整除，跳出for循环
            if i % x == 0:
                break
        # 不能取整说明是质数添加到里列表list_num中
        # 这里用到了for else，需要注意一下
        else:
           count = count + 1
    print(count)
if __name__ =='__main__':
    start = time()
    maan(1,100000)
    end = time()
    print(end - start)



