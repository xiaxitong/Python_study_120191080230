#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:ab.py
# author:16546
# datetime:2021/4/11 15:43
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os
#打开上级目录中的文件
with open(r'../b_file/a.txt') as files:
    print(files.read())
