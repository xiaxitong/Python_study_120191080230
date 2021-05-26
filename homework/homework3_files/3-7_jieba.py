#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3-7.py
# author:16546
# datetime:2021/4/11 9:33
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
# 对一篇中文文献, ;利用jieba库,进行词频统计分析找出文章的关键词(取词频最高的前10个词语,作为文章的关键字);
'''

import jieba
import jieba.analyse
text = ''
#jieba.load_userdict("jieba_dict.txt")  # 用户自定义词典 （用户可以自己在这个文本文件中，写好自定制词汇）
f = open('jieba_text.txt', 'r', encoding='utf8')  # 要进行分词处理的文本文件 (统统按照utf8文件去处理，省得麻烦)
lines = f.readlines()
for line in lines:
    text += line

# seg_list = jieba.cut(text, cut_all=False)  #精确模式（默认是精确模式）
seg_list = jieba.cut(text)  # 精确模式（默认是精确模式）
print("[精确模式]: ", "/ ".join(seg_list))

tags = jieba.analyse.extract_tags(text, topK=10)
print("关键词:    ", " / ".join(tags))
