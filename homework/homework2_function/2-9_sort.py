#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2-9.py
# author:16546
# datetime:2021/4/2 14:50
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
# 定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);
def Account():
    arr = list(input().split(","))
    ar = list(map(int,arr))

    #map(function,~)
    #把函数依次作用在list中的每一个元素上，得到一个新的list并返回
    #还可用于转换序列中的元素的数据类型

    ar.sort()

    # 直接改变输入的列表，没有返回值
    print(ar)

if __name__ == '__main__':
    Account()
