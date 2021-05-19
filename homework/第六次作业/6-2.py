#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:6-1.py
# author:16546
# datetime:2021/5/19 15:45
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
class Student(object):
    # 构造方法
    def __init__(self, name, age, scores):
        self.__name = name     # 姓名
        self.__age = age       # 年龄
        self.__scores = scores # 分数
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_course(self):
        return max(self.__scores)
if __name__ == "__main__":
    stu = Student('小丸子', 18, [89, 90, 91])
    print("姓名：%s" % (stu.get_name()))
    print("年龄：%s" % (stu.get_age()))
    print("最高分：%s" % (stu.get_course()))