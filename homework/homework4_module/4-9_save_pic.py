#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:4-9_save_pic.py
# author:16546
# datetime:2021/5/25 18:08
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
# 从网络上下载一张图片，保存到计算机的指定目录；（requests和os模块）
'''

import requests

import os

url="https://ps.ssl.qhmsg.com/bdr/720__/t017843e759f2628d1f.jpg"

d='E:\python_study_exercise\homework\homework4_module\picture4'

path=d+url.split('/')[-1]

try:

    if not os.path.exists(d):

        os.mkdir(d)

    if not os.path.exists(path):

        r=requests.get(url)

        r.raise_for_status()

        with open(path,'wb') as f:

            f.write(r.content)

            f.close()

            print("图片保存成功")

    else:

        print("图片已存在")

except:

    print("图片获取失败")