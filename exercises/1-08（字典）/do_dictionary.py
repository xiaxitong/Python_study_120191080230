#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_dictionary.py
# author:16546
# datetime:2021/3/14 20:01
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == "__main__":
    dict1 = {'Id': 1254, 'Name': '张三', 'Class': 6, 'Age': 19}
    dict2 = {'Id1': 1268, 'Id2': 1248, 'Id3': 9268, 'Id4': 1468, 'Id5': 1898,
             'Name1': 'a', 'Name2': 'aa', 'Name3': 'aaa', 'Name4': 'aaaa', 'Name5': 'aaaaa'}
    print(dict1['Id'])
    print(dict2['Name5'])
    dict1['Height'] = 180
    dict1['Age'] = 22
    del dict1['Class']
    print(dict1)