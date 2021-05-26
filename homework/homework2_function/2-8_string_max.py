#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2-8.py
# author:16546
# datetime:2021/4/2 14:50
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
# 请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
#  例如，输入 aaaabbc，输出：a:4
'''

def Max_str():
    str = input("输入一个字符串：")
    l = list(str)
    print(f'出现次数最多的字符是：{max(l,key=l.count)}\n'
          f'其出现次数为：{l.count(max(l,key=l.count))}')

    #max(序列名，key=序列名.count)得到的是一个序列中出现次数最多的字符
    #前面加上  .count() 得到的才是该次数
if __name__ == '__main__':
    Max_str()