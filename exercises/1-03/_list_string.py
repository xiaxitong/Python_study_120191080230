#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:_list_string.py
# author:16546
# datetime:2021/3/4 15:52
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def reverseWords(input):
    inputWords = input.split(" ")
    inputWords=inputWords[-1::-1]
    output= ' '.join(inputWords)
    return output
if __name__=="__main__":
    input = 'a b c d e f'
    rw = reverseWords(input)
    print(rw)