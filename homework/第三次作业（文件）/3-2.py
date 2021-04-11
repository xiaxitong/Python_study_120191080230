#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3-2.py
# author:16546
# datetime:2021/4/5 8:31
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == '__main__':
    list = []
    filename = 'pyhton文件库/input.txt'
    try:
      with open (filename,encoding = 'utf-8') as file_object:
          list = file_object.readlines()
          #redlines（）用于逐行读取文件到列表中

      for i in  range(len(list)):
          print(f'#第{i+1}行： {list[i].rstrip()}')
          #rstrip() 用于消除换行符

    except FileNotFoundError:
        print("文件不存在！")

