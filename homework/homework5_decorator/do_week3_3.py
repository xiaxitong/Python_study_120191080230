#!/usr/bin/env python
#-*-coding:utf-8-*-

#file:do_week3_3.py
#author:HP
#datetime:2021/4/25 20:13
#software: PyCharm
'''
this is function  description 
'''
# import module your need

'''
  编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
'''
def outer(func):
    def inner():
        print("ID:")
        ID = input()
        print("Key:")
        Key =input()
        if(ID == '123456')and(Key == '123456'):
            func()
        else:
            exit(0)
    return inner

@outer
def func():
    print("-------func-------")
    pass

func()
