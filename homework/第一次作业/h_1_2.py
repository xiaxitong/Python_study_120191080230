#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:h_1_2.py
# author:16546
# datetime:2021/3/23 16:11
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == "__main__":
    dic = { 'a': '89' ,
           'b' : '24' ,
            'c': '56' ,
           'd': '78' ,
          'e':  '98' ,
            'f' : '58' ,
           'g' : '79' ,
            'h' : '99' ,
            'i' : '88' ,
            'j' : '74' ,}
    print("大于80分的同学：")
    for k, v in dic.items():
        if v > '80 ':
            print( f'{k.title() } : {v.title()}')