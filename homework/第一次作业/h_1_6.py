#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:h_1_6.py
# author:16546
# datetime:2021/3/24 15:31
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
#    a = 0
#   b = 1
 #   print(f'{a},{b}')
  #  while a<100 or b<100:
   #     a = a + b
    #    b = b + a
     #   print(f'{a},{b},')
if __name__ == '__main__':
    list = [0,1]
    a = 0
    b = 1
    while a < 100 and b < 100:
        a = a + b
        b = b + a
        if a < 100 and b < 100:
            list.append(a)
            list.append(b)
    print(list)