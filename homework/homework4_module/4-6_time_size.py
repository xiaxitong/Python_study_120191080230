#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:xianshi_file.py
# author:16546
# datetime:2021/4/18 9:33
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
# 通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
import  os
import time
base_dir = 'E:\python_study_exercise\homework\homework4_module/file_size_time'
list = os.listdir(base_dir)
for i in list:
    file_path = os.path.join(base_dir,i)
    if (os.path.isfile(file_path)):
          print(f'文件名：{i}',end=' ')
          print(f'文件大小：{os.path.getsize(file_path)}',end = ' ')
          print(f'修改时间：{time.ctime(os.path.getctime(file_path))}')
          #os.path 模块里面的是文件路径
          #时间输出要用到time模块
    else:
          print(f'文件名：{i}', end=' ')
          print(f'修改时间：{time.ctime(os.path.getctime(file_path))}')
# print(l_time)