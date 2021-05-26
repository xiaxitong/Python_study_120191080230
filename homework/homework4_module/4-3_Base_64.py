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
'''
# 从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
#         Tom   admin   XXXXX
#         Jack   root      XXXXX
'''

import base64
if __name__ == '__main__':
    l = list(input().split(','))

    # a = l[0].split(' ')[2]
    # print(str(base64.b64encode(b'a')))
    filename = 'Base_64.txt'
    for i in l :
        i.split(' ')[2] = str(i.split(' ')[2])
    # print(type(l[0].split(' ')[2]))
    for i in l:
        a = i.split(' ')[2]
        b = str(base64.b64encode(a.encode('utf-8')))
    with open(filename, 'w', encoding='utf-8') as f:
        for i in l :
           f.write(i+'\n')