#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:h_1_3.py
# author:16546
# datetime:2021/3/23 16:30
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == "__main__":
    list1 = list(range(1,11,2))
    list2 = list(range(1,11,3))
    print(f'"输出列表1的值："{list1}')
    print(f'"输出列表2的值："{list2}')
    for i in list1:
        for j in list2:
            if j==i:
                print(j)
