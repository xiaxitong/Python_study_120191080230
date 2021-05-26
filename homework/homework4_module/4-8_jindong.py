#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:4-8_jindong.py
# author:16546
# datetime:2021/5/25 18:08
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
# #京东二面笔试题
# 1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
# 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
'''

import random
import collections

with open("ip.txt", "w", encoding="utf-8") as file1:
    for i in range(1200):
        ip = "172.25.254." + str(random.randint(1, 255)) + "\n"
        file1.write(ip)
try:
    with open("ip.txt", "r", encoding="utf-8") as file2:
        data = file2.readlines()
except FileNotFoundError:
    print("文件不存在或被删除!")

c = collections.Counter(data)
c_list = c.most_common(10)
for key in c_list:
    print("ip:{}  出现次数:{}".format(key[0].rstrip(), key[1]))