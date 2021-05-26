#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:h_1_4.py
# author:16546
# datetime:2021/3/23 16:34
# software: PyCharm
'''
this is functiondescription
'''
# import module your need


if __name__ == '__main__':
    year = input("输入年份：")
    if int (year)%4 ==0:
        print(f'{year}是闰年。')
    else:
        print(f'{year}不是闰年。')
