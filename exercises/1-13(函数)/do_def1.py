#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_def.py
# author:16546
# datetime:2021/3/15 14:07
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def apple_price(price, height):
    print(f'价格为: {int(price) * int(height)}')
if __name__ =="__main__":
    a = input("单价：")
    b = input("数量: ")
    apple_price(a,b)