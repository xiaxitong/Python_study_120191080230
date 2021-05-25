#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3-3.py
# author:16546
# datetime:2021/4/5 9:27
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
# 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出

if __name__ == '__main__':
    filename = 'pyhton文件库/学生成绩.txt'
    name = []
    id = []
    score = []
    with open(filename,'r') as file_object:
           next(file_object)
           li = file_object.readline()
           while li:
               l = li.split(' ')
               name.append(l[0])
               id.append(l[1])
               score.append(l[2].rstrip())
               li = file_object.readline()
    #排序
    for i in range(len(score)):
        min_s = i
        for j in range(i+1,len(score)):
            if int(score[min_s])>int(score[j]):
                min_s = j
        score[i],score[min_s] = score[min_s],score[i]
        name[i], name[min_s] = name[min_s], name[i]
        id[i], id[min_s] = id[min_s], id[i]
    with open(filename,'w') as f:
        for i in range(len(score)):
            f.write(name[i]+' ')
            f.write(id[i] + ' ')
            f.write(score[i] + '\n')
