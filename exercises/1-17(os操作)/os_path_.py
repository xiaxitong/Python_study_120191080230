#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:os_path_.py
# author:16546
# datetime:2021/4/11 15:27
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os

# 创建目录test
# os.mkdir("test")

# 删除目录
# print(os.getcwd())
# os.rmdir("E:/python_study_exercise/exercise/test")

path = "E:/python_study_exercise/exercise/test"
t = os.path.splitext(path)
t1 = os.path.split(path)
t2 = os.path.basename(path)
t3 = os.path.dirname(path)
print(t)
print(t1)
print(t2)
print(t3)