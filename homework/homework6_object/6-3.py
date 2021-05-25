#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:6-3.py
# author:16546
# datetime:2021/5/19 17:21
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
class dictclass(object):
    def __init__(self,d):
        self.__dic = d
    def del_dict(self,key):
        del self.__dic[key]
    def get_dict(self,key):
        point_value = self.__dic.get(key,'not found')
        print(point_value)
    def get_key(self):
        list = []
        for name in self.__dic.keys():#遍历键
            list.append(name)
        print(list)
    def update_dict(self,d2):
        list = []
        d1 = {}
        d1.update(self.__dic)
        d1.update(d2)
        #合并字典的函数
        for v in d1.values():#访问值
            list.append(v)
        print(list)

if __name__ == "__main__":
    d = {
        'jen':'agf',
        'af':'fag',
        'fag':'fafgf'
    }
    dict = dictclass(d)
    # dict.del_dict('jen')

    # dict.get_dict('af')

    # dict.get_key()

    dict.update_dict({'faf':'agfag'})
    # print(d)