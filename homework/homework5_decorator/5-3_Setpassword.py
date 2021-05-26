#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:设置账户密码.py
# author:16546
# datetime:2021/4/27 16:38
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
#编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）

def decrator(func):
    username = input("输入用户名：")
    secret = input("输入密码：")
    if secret == '0000':
        def wrapper():
            func()
        return wrapper
    else:
        return 0

@decrator
def login():
    print("登录成功！")

login()