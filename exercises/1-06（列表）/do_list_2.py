#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_list_2.py
# author:16546
# datetime:2021/3/14 18:59
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == "__main__":
    list = [80,90,98,78,58,65,98,78,62,64]
    l_max = max(list)
    l_min = min(list)
    l_general = 0
    for i in list:
        l_general += i
    l_avg = l_general/10
    print(f'最大值： {l_max}\n最小值：{l_min}\n总分：{l_general}\n平均值：{l_avg}')

