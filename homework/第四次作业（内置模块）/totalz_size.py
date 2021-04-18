#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:totalz_size.py
# author:16546
# datetime:2021/4/18 10:21
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import  os
base_dir = 'E:\python_study_exercise\homework\第四次作业\新建文件夹'
list = os.listdir(base_dir)
size = []
for i in list:
    file_path = os.path.join(base_dir,i)
    if (os.path.isfile(file_path)):
        size.append(os.path.getsize(file_path))
for i in size:
    sum = i
    sum = sum + i
print(sum)