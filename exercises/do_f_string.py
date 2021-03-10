#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_f_string.py
# author:16546
# datetime:2021/3/10 16:45
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ =='__main__':
    movie = '流浪地球'
    ticket = 45.9
    count = 15
    total = ticket*count
    print(
    f'电影：{movie}\n'
    f'人数：{count}\n'
    f'单价：{ticket}\n'
    f'总票价：{total}'
    )