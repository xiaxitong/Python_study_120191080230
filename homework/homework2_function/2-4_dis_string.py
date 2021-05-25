#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2-4.py
# author:16546
# datetime:2021/4/2 14:50
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
#写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;

def do_judge():
    str = input("输入字符串：")
    l = list(str)
    print(l)
    alpha = 0
    digit = 0
    tab = 0
    str = 0
    for i in l:
        if i.isalpha():
            alpha = alpha + 1
        elif i.isdigit() :
            digit = digit + 1
        elif i == ' ':
             tab = tab + 1
        else:
            str = str + 1
    print(f'字母个数为：{alpha}\n数字个数为：{digit}\n空格个数为：{tab}\n'
          f'其他字符个数为：{str}')
if __name__ == '__main__':
    do_judge()