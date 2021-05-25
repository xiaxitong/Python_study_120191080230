#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2-1.py
# author:16546
# datetime:2021/4/2 14:49
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
#写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。

def do_length():
    str = input("输入字符串：")
    a = len(str)
    l = list(input("输入列表：").split(','))
    b = len(l)
    t = tuple(input("输入元组：").split(','))
    c = len(t)
    print(f'字符串长度为:{a}\n列表长度为：{b}\n元组长度为：{c}')
if __name__ =='__main__':
    do_length()