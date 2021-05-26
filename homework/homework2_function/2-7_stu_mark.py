#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2-7.py
# author:16546
# datetime:2021/4/2 14:50
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
# 随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;
#     A---成绩>=90;
#     B-->成绩在 [80,90)
#     C-->成绩在 [70,80)
#     D-->成绩<70
'''

import random
def do_mark():
    l = list(random.randint(0,100) for i in range(20))
    A = []
    B = []
    C = []
    D = []
    for i in l :
        if i >= 90:
            A.append(i)
        elif i >= 80 and i < 90:
            B.append(i)
        elif i >= 70 and i < 80:
            C.append(i)
        else:
            D.append(i)
    print(f'A:{A}\nB:{B}\nC:{C}\nD:{D}')

if __name__ == '__main__':
    do_mark()