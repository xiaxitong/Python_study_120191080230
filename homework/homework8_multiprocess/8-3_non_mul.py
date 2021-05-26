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
'''
3  多进程练习：
计算1～100000之间所有素数的个数， 要求如下:
- 编写函数判断一个数字是否为素数，然后统计素数的个数；
-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。
'''
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



