#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3-5.py
# author:16546
# datetime:2021/4/11 9:33
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == "__main__":

    filename = 'E:\python_study_exercise\homework\第三次作业（文件）\pyhton文件库\Blowing in the wind.txt'
    with open(filename,'r') as file1:
        l = file1.readlines()
    l.insert(0,'Blowing in the wind\n')
    l.insert(1,'Bob Dylan\n')
    #可以在列表的任意位置插入元素

    l.append('\n1962 by Warner Bros.Inc')
    print(l)
    with open(filename,'w') as file2:
        for i in l:
            file2.write(i)
            #write函数只能写入字符串，不能直接将列表写入


