#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2-10.py
# author:16546
# datetime:2021/4/2 14:50
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def Cacluate(str,a,b):
    if str == '+':
        print("进行加法运算")
        print(a+b)
    elif str == '-':
        print("进行减法运算")
        print(abs(a-b))
    elif str == '*':
        print("进行乘法运算")
        print(a*b)
    elif str == '/':
        print("进行除法运算")
        print(a/b)

if __name__ == '__main__':
    str1 = input()

    #字符和数字不要同时输入
    x,y = map(int,input().split(','))

    #map()用于一次输入多个数
    #分隔符不能是中文状态的符号
    Cacluate(str1,x,y)

