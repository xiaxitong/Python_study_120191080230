#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:4-4_login.py
# author:16546
# datetime:2021/5/25 18:30
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
# 模拟用户登录:
#　我们先在程序中向网站发出登录请求，也就是提交包含登录信息的表单（用户名、密码等）。
# 从响应中得到cookie，今后在访问其他页面时也带上这个cookie，就能得到只有登录后才能看到的页面。
'''


import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

#登录后才能访问的网页
url = 'http://ssfw.xmu.edu.cn/cmstar/index.portal'

#浏览器登录后得到的cookie，也就是刚才复制的字符串
cookie_str = r'JSESSIONID=xxxxxxxxxxxxxxxxxxxxxx; iPlanetDirectoryPro=xxxxxxxxxxxxxxxxxx'

#把cookie字符串处理成字典，以便接下来使用
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

#在发送get请求时带上请求头和cookies
resp = requests.get(url, headers = headers, cookies = cookies)

print(resp.content.decode('utf-8'))