#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:h_1_9.py
# author:16546
# datetime:2021/3/24 16:45
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == '__main__':
    number = input("输入这个数字：")
    for i in range(1,11):
        g_number = input("输入猜测的数字：")
        if g_number == number:
            print("猜对了")
            break
    print("猜错了")
