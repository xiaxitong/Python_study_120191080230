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
'''
三、定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})
'''
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