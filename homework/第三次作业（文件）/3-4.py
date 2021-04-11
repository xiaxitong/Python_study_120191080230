#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3-4.py
# author:16546
# datetime:2021/4/5 10:34
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os
import sys
if __name__ == "__main__":
    path0 = 'E:\python_study_exercise\homework\第三次作业（文件）\第四题.img'
    path1 = 'E:\python_study_exercise\homework\第三次作业（文件）\第四题.img'+'\\'
    sys.path.append(path1)
    #python的默认搜索路径为当前目录，若要访问同级或上级目录，则将路径加到sys.path模块中。。

    print(sys.path)
    #sys.path是python的搜索模块的路径集
    files = os.listdir(path0)
    # print(files)
    for filename in files:
        #此处的filename只是包含要打开的文件名，而没有路径

        portion = os.path.splitext(filename)
        #将文件后缀与文件名分隔开

        if portion[1] == '.png':
            newname = portion[0]+'.jpg'
            filenamedir = path1 + filename
            newnamedir = path1 + newname
            os.rename(filenamedir,newnamedir)
            #rename需要的是文件的绝对路径及文件名
