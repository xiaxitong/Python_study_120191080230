#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:6-1.py
# author:16546
# datetime:2021/5/19 17:19
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
       实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
'''
class Dog:
    # 构造方法
    def __init__(self):
        self.list = []
        # self.list[0] = {'color':'yellow','count':3,'price':888}
        # self.list[1] = {'color':'black','count':5,'price':999}
        # self.list[2] = {'color':'white', 'count': 2, 'price': 898}
    def push(self,d):
        self.list.append(d)
    def Sale(self):
        Color = input("输入想要的狗的颜色：")
        if Color == 'yellow':
            i = 0
            if self.list[i]['count'] !=0:
                print("购买成功！")
                self.list[i]['count'] = self.list[i]['count']-1
            else:
                print("该颜色的狗已卖完，请重新选择：")
        if Color == 'black':
            i = 0
            if self.list[i]['count'] !=0:
                print("购买成功！")
                self.list[i]['count'] = self.list[i]['count']-1
            else:
                print("该颜色的狗已卖完，请重新选择：")
        if Color == 'white':
            i = 0
            if self.list[i]['count'] !=0:
                print("购买成功！")
                self.list[i]['count'] = self.list[i]['count']-1
            else:
                print("该颜色的狗已卖完，请重新选择：")
    def pop_count(self):
        for i in self.list:
            print(i['count'])
if __name__ == "__main__":
    d = Dog()
        #([{'color':'yellow','count':3,'price':888},{'color':'black','count':5,'price':999},{'color':'white', 'count': 2, 'price': 898}])
    d.push({'color':'yellow','count':3,'price':888})
    d.push({'color':'black','count':5,'price':999})
    d.push({'color':'white', 'count': 2, 'price': 898})
    d.Sale()
    d.Sale()
    d.pop_count()













