#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:deque.py
# author:16546
# datetime:2021/4/18 8:26
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
# 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
#     提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
'''
from collections import deque
from datetime import datetime
if __name__ == "__main__":
    l1 = deque([1,2,3,4,5,6,7,8,9,10])
    #deque表示双向列表，用于在头部进行删除和插入操作，分别用到函数：popleft(),appendleft()

    l2 = [1,2,3,4,5,6,7,8,9,10]
    # d1_list = datetime.now()
    # for i in l2:
    #    l1.append(i)
    #    l1.insert(0,i)
    # d2_list = datetime.now()
    # print(d2_list.timestamp()-d1_list.timestamp())
    #进行太快，无法得出秒级的差值

    d1_deque = datetime.now()
    for i in l2:
        l1.appendleft(i)
    d2_deque = datetime.now()
    #now()记录当前的日期和时间
    print(d2_deque.timestamp() - d1_deque.timestamp())
    #timestamp表示时间戳
