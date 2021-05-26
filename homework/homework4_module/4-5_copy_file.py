#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:4-5_copy_file.py
# author:16546
# datetime:2021/5/25 18:08
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
#通过Python来模拟实现一个txt文件的拷贝过程;
'''

import os
def copydd(dir1, dir2):
    # 获取被复制目录中的所有文件信息
    dlist = os.listdir(dir1)
    # 创建新目录
    os.mkdir(dir2)
    for f in dlist:
    # 为遍历的文件添加目录路径
      file1 = os.path.join(dir1, f)  # 源
      file2 = os.path.join(dir2, f)  # 目标
    # 判断是否是文件
      if os.path.isfile(file1):
          mycopy(file1, file2)  # 调用自定义文件复制函数来复制文件
    # 判断是否是目录
      if os.path.isdir(file1):
          copydd(file1, file2)  # 递归调用自己，来实现目录的复制


# 测试

copydd("./aa", "./dd")

