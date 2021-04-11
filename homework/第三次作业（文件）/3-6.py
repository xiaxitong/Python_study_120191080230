#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3-6.py
# author:16546
# datetime:2021/4/11 9:33
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from collections import Counter
def getText():
    with open("E:\python_study_exercise\homework\第三次作业（文件）"
              "\pyhton文件库\《老人与海》[英文版].txt",encoding='utf-8')  as file:
        txt = file.read()
        #read()方法得到的是一个字符串，而不是列表
    txt = txt.lower()
    for ch in '!".,;:?(){}~-\n':
        txt = txt.replace(ch,"")
        #不用遍历文档，可以以要修改的对象为主体，直接用相关函数修改
    return txt
if __name__ == "__main__":
    str = getText()
    l = str.split(' ')
    #split()分割字符串并自动将其转换成列表

    c= Counter(l)
    cc = c.most_common(2)
    #Counter类容器是专门用来给序列计数的

    print(cc)




