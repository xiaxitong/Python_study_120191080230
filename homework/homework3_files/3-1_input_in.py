#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3-1.py
# author:16546
# datetime:2021/4/5 8:31
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
# 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，将读入的字符串存于列表;
# 然后将列表里面的内容写入到文件input.txt中；

if __name__ == '__main__':
    l = list(input().split(' '))
    print(l)
    filename = 'pyhton文件库/input.txt'
    with open(filename,'w') as file_1:
        for i in l:
            file_1.write(i+'\n')
input
#for 循环可以单个写入列表元素，并且加上换行符
#直接写入列表元素需要将其转化成字符串类型
#python只能将字符串写入文本文件
