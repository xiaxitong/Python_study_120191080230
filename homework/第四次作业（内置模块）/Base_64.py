#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:Base_64.py
# author:16546
# datetime:2021/4/18 8:28
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import base64
if __name__ == '__main__':
    l = list(input().split(','))

    # a = l[0].split(' ')[2]
    # print(str(base64.b64encode(b'a')))
    filename = 'Base_64的学生加密信息.txt'
    for i in l :
        i.split(' ')[2] = str(i.split(' ')[2])
    # print(type(l[0].split(' ')[2]))
    for i in l:
        a = i.split(' ')[2]
        b = str(base64.b64encode(a.encode('utf-8')))
    with open(filename, 'w', encoding='utf-8') as f:
        for i in l :
           f.write(i+'\n')