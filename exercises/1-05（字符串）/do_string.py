#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_string.py
# author:16546
# datetime:2021/3/10 16:56
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ =='__main__':
    s_true = 'rld'
    string = 'hello world'
    s_false = 'python'
    print("存在")
    print (string.find(s_true,len(s_true)))
    print("不存在")
    print(string.find(s_false,len(s_false)))
    print("替换后的字符串")
    print(string.replace('hello','hi'))
    print("打印字符串的长度")
    print(len(string))