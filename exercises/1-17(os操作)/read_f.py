#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:read_f.py
# author:16546
# datetime:2021/4/11 15:59
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os
with open('学生信息.txt','r',encoding= 'utf-8') as f:
    print(f.read())