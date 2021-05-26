#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:h_1_10.py
# author:16546
# datetime:2021/3/24 16:50
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == '__main__':
    list = ['I', 'like', 'Python', 'I', 'like', 'English', 'too']
    dic = {'I': '0', 'like': '0', 'Python': '0', 'English': '0', 'too': '0'}
    for j in list:
        count = 0
        for i in list:
            if i == j:
                count = count + 1
        dic[j] = count
    print(dic)

