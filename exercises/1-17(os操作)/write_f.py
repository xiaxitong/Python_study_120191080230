#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:write_f.py
# author:16546
# datetime:2021/4/11 16:01
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os
student = []
with open('学生信息.txt','r',encoding = 'utf-8') as file:
    for line in file.readlines():
        student.append(line.rstrip())
    length = len(student)
    for i in range(1,length):
        for j in range(i,length):
            if int(student[i].split(" ")[2])>int(student[j].split(" ")[2]):
                t = student[i]
                student[i] = student[j]
                student[j] = t
with open('学生信息1.txt','w',encoding = 'utf-8') as f:
    for i in student:
        f.write(i+'\n')