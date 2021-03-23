#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:h_1_1.py
# author:16546
# datetime:2021/3/23 15:31
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == "__main__":
     l = list(range(0,51))
     print("偶数如下： ")
     for i in l:
         if i%2 == 0:
             print(i)
     print("奇数如下： ")
     for i in l:
         if i%2 == 1:
             print(i)
     print("质数如下： ")
     for i in l:
         n = 0
         for j in range(1,i+1):
             if i%j == 0:
                 n = n + 1
         if n==2:
             print(i)
     print("能同时被2和3整除的数： ")
     for i in l:
         if i%2 == 0 and i%3 == 0:
             print(i)

