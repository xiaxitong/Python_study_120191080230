#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2-6.py
# author:16546
# datetime:2021/4/2 14:50
# # software: PyCharm
# '''
# this is functiondescription
# '''
# import module your need


#打印输出n以内的斐波那契数列

def do_Fibonacci():
    n = int(input("输入n的值："))
    i = 0
    j = 1
    print(0,end = ',')
    while j < n :
        i,j = j,j + i
        if j< n :
            print(j,end = ',')
if __name__ == '__main__':
    do_Fibonacci()

# def Fibonacci(n):
#     a, b = 0, 1
#     for i in range(n + 1):
#         a, b = b, a + b    # 注意这个表达式的含义
#     return a
#
# for i in range(10):
#     print(Fibonacci(i), end=' ')