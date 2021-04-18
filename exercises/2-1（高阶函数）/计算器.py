#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:计算器.py
# author:16546
# datetime:2021/4/18 15:28
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def add(x,y):
    print (x+y)
def sub(x,y):
    print (abs(x-y))
def mul(x,y):
    print (x*y)
def div(x,y):
    print(x/y)
def calculate(x,y,f):
    f(x,y)
if __name__ == '__main__':
    a = int(input("请输入要计算第一个数："))
    b = int(input("请输入要计算第二个数："))
    #input默认输入数据为字符型

    s = input("请输入要进行何种运算：")
    if (s =="加法"):
        calculate(a,b,add)
    elif (s == '减法'):
        calculate(a,b,sub)
    elif (s == "乘法"):
        calculate(a,b,mul)
    elif(s=="除法"):
        calculate(a,b,div)

