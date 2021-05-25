#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2-5.py
# author:16546
# datetime:2021/4/2 14:50
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
#写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;

#如何遍历修改字典中的值
#将字典中的键和值分别放在一个列表中，然后将元素依次对应修改
def do_dic():
    dic = {'1': 'adf', '2': 'bl', '3': 'ccrge'}
    list1 = []
    for v in dic.values():
        l = list(v)
        # print(l)
        length = len(l)
        if len(l)>2:
            for i in range(2,length):
                del l[2]
        list1.append("".join(l))
    list2 = []
    for k in dic.keys():
        list2.append(k)
    for i in range(0,len(list1)):
        dic[list2[i]] = list1[i]
    # print(list1)
    # dic['1'] = list1[0]
    # dic['2'] = list1[1]
    # dic['3'] = list1[2]
    print(dic)
if __name__ == '__main__':
    do_dic()