#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3-7.py
# author:16546
# datetime:2021/4/11 9:33
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import jieba
if __name__ == '__main__':
    ls = jieba.lcut("中国是国外开发和")
    print(ls)