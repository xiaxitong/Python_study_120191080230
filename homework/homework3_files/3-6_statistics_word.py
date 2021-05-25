#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3-6.py
# author:16546
# datetime:2021/4/11 9:33
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
# 对一篇英文小说，进行词频统计，输出前20个出现频率最高的单词；
#         英文小说"老人与海"     链接：https://pan.baidu.com/s/1goqK3zF8VBUFuD_2ezfZ7Q   提取码：mv04
#     提示：
#     1 可以先定义一个函数，专门来处理英文文章的读取问题；读取时，解决大小写问题，以及标点符号问题（如，将标点符号都替换成空格）；

from collections import Counter
def getText():
    with open("E:\python_study_exercise\homework\第三次作业（文件）"
              "\pyhton文件库\《老人与海》[英文版].txt",encoding='utf-8')  as file:
        txt = file.read()
        #read()方法得到的是一个字符串，而不是列表
    txt = txt.lower()
    for ch in '!".,;:?(){}~-\n':
        txt = txt.replace(ch,"")
        #不用遍历文档，可以以要修改的对象为主体，直接用相关函数修改
    return txt
if __name__ == "__main__":
    str = getText()
    l = str.split(' ')
    #split()分割字符串并自动将其转换成列表

    c= Counter(l)
    cc = c.most_common(2)
    #Counter类容器是专门用来给序列计数的

    print(cc)




