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
'''
# 创建一个文件Blowing in the wind.txt
# 在文件头部插入歌名“‘Blowing’ in the wind”
# 在歌名后插入歌手名“Bob Dylan”
# 在文件末尾加上字符串“1962 by Warner Bros.Inc”
# 在屏幕上打印文件内容
'''

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


