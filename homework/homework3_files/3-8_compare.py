#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3-8.py
# author:16546
# datetime:2021/4/11 9:33
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
程序用python3运行时，可将当前路径下的aa.txt文件读取后，按空格分割成一系列的单词，
然后统计这些单词出现的次数，按频率从大到小排序后，写入ar.txt文件中。
涉及的语法有：
1、中英文混合对齐；
2、collections.Counter；
3、获取当前路径、文件读写、路径与文件名组合、随机数生成。。。
'''
import os
from random import choice, randint
from collections import Counter
from string import ascii_letters as letters

# 假设要读取文件名为aa，位于当前路径
filename = 'aa.txt'
dirname = os.getcwd()
fname = os.path.join(dirname, filename)

# 注释掉的程序段，用于测试脚本，它生成20行数据，每行有1-20随机个数字，每个数字随机1-20
# '''
lines = []
for i in range(20):
    line = []
    for j in range(randint(1, 20)):
        line.append(''.join([choice(letters) for c in range(randint(1, 10))]))
    lines.append(' '.join(line))
with open(fname, 'w') as f:
    f.write('\n'.join(lines))
# '''
with open(fname) as f:
    s = f.read()

counter = Counter(s.replace('\n', ' ').split(' '))


# 格式化要输出的每行数据，首尾各占8位，中间占18位
def geshi(a, b, c):
    return alignment(str(a)) + alignment(str(b), 18) + alignment(str(c)) + '\n'


# 中英文混合对齐 ，参考http://bbs.fishc.com/thread-67465-1-1.html
# 汉字与字母 格式化占位 format对齐出错 对不齐 汉字对齐数字 汉字对齐字母 中文对齐英文
# alignment函数用于英汉混合对齐、汉字英文对齐、汉英对齐、中英对齐
def alignment(str1, space=8, align='left'):
    length = len(str1.encode('gbk'))
    space = space - length if space >= length else 0
    if align in ['left', 'l', 'L', 'Left', 'LEFT']:
        return str1 + ' ' * space
    elif align in ['right', 'r', 'R', 'Right', 'RIGHT']:
        return ' ' * space + str1
    elif align in ['center', 'c', 'C', 'Center', 'CENTER', 'centre']:
        return ' ' * (space // 2) + str1 + ' ' * (space - space // 2)
    return 'Unknow align format'


title = geshi('序号', '词', '频率')
results = []
# 要输出的数据，每一行由：序号(占8位)词(占20位)频率(占8位)+'\n'构成，序号=List.index(element)+1
for i, (w, c) in enumerate(counter.most_common(), 1):
    results.append(geshi(i, w, c))

# 将统计结果写入文件ar.txt中
writefile = 'ar.txt'
wpath = os.path.join(dirname, writefile)
with open(wpath, 'w') as f:
    f.write(''.join([title] + results))