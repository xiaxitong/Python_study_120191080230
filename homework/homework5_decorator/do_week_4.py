#!/usr/bin/env python
#-*-coding:utf-8-*-

#file:do_week_4.py
#author:HP
#datetime:2021/4/25 20:28
#software: PyCharm
'''
this is function  description 
'''
# import module your need
'''
     编写装饰器来实现，对目标函数进行装饰,计算函数的运行耗时，
    分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
     三个目标函数分别为：
     A 打印输出20000之内的素数；
     B 计算整数2-10000之间的素数的个数；
     C 计算整数2-M之间的素数的个数；
'''
import time

def outer(func):
    def inner():
        start_time =time.time()
        func()
        end_time =time.time()
        print("run time:",end_time-start_time)

    return inner

@outer
def func():
    for num in range(2, 20000 + 1):
        # 素数大于 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

@outer
def func1():
    a = 0;
    for num in range(2, 10001):
        # 素数大于 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                a += 1
    print(a)
    return a

@outer
def func2():
    a = int(input("输入区间最大值:"))
    b=0
    for num in range(2, a):
        # 素数大于 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
                b += 1

#无参数，无返回
func()
#有返回值
func1()
#有参数
func2()