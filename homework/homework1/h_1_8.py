#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:h_1_8.py
# author:16546
# datetime:2021/3/24 16:11
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == '__main__':
    list = []
    for i in range(0,3):
        list.append(0)
    list[0] = {'工号':'123','姓名':'张三','工资':'8000','工龄':'4年'}
    list[1] = {'工号':'124', '姓名': '李三', '工资': '5400', '工龄': '4年'}
    list[2] = {'工号': '154', '姓名': '王麻子', '工资': '9870', '工龄': '4年'}
    for x in range(0,3):
        for y in range(x+1,3):
            if(int(list[y]['工资']) > int(list[x]['工资'])):
                list[y],list[x] = list[x],list[y]
    for i in list:
        print(i)
