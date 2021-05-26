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
'''
二 定义一个学生Student类。有下面的类属性：
1 姓名 name
2 年龄 age
3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:
'''
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