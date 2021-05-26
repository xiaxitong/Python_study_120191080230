#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:6-4.py
# author:16546
# datetime:2021/5/19 17:22
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
# 班级类
'''
四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
      封装方法，求单个学生的总分，平均分，以及打印学生的信息。
'''
class Class_NO(object):
    def __init__(self, name):
        self.grade_class_name = name
        self.students = []

    def set_grade_class_name(self, name):
        self.grade_class_name = name

    def get_grade_class_name(self):
        return self.grade_class_name

    def add_student(self, student):
        self.students.append(student)

    def get__classNo_max_total_score(self):
        student_total_score = []
        for i in self.students:
            student_total_score.append(i.get_student_total_score())  ##########
        # print (student_total_score)
        max_student_total_score = max(student_total_score)
        return max_student_total_score

    def get_classNo_chinese_avg_score(self):
        student_chinese_score = []
        for i in self.students:
            student_chinese_score.append(i.get_chinese_score())
        return sum(student_chinese_score) / len(self.students)

    def get_classNo_math_avg_score(self):
        student_math_score = []
        for i in self.students:
            student_math_score.append(i.get_math_score())
        return sum(student_math_score) / len(self.students)


# 学生类
class Student(object):
    def __init__(self, name, grade_class_no):
        self.name = name
        self.grade_class_no = grade_class_no
        self.__chinese_score = None
        self.__math_score = None
        self.__total_score = None

    def set_chinese_score(self, score):
        if score >= 0 and score <= 100 and isinstance(score, (int, float)):
            self.__chinese_score = score
        else:
            print("你输入的分数不是数字类型，或者不在0-100分数的范围内")

    def get_chinese_score(self):
        return self.__chinese_score

    def set_math_score(self, score):
        if score >= 0 and score <= 100 and isinstance(score, (int, float)):
            self.__math_score = score
        else:
            print("你输入的分数不是数字类型，或者不在0-100分数的范围内")

    def get_math_score(self):
        return self.__math_score

    def get_student_total_score(self):
        self.__total_score = self.__chinese_score + self.__math_score
        return self.__total_score

    def get_student_avg_score(self):
        return sum([self.__chinese_score, self.__math_score]) / 2

    def get_student_max_score(self):
        return max(self.__chinese_score, self.__math_score)


if __name__ == "__main__":
    s = Student("zita", "三年二班")
    s.set_chinese_score(100)
    s.set_math_score(80)
    print("%s的平均分是:%s" % (s.name, s.get_student_avg_score()), ",", "%s的总分是:%s" % (s.name, s.get_student_total_score()),
          ",", "%s的最高分是:%s" % (s.name, s.get_student_max_score()))
    t = Student("tim", "三年二班")
    t.set_chinese_score(88)
    t.set_math_score(62)
    print("%s的平均分是:%s" % (t.name, t.get_student_avg_score()), ",", "%s的总分是:%s" % (t.name, t.get_student_total_score()),
          ",", "%s的最高分是:%s" % (t.name, t.get_student_max_score()))
    c = Class_NO("三年二班")
    c.add_student(s)
    c.add_student(t)
    print("%s总分最高分是:%s" % (c.get_grade_class_name(), c.get__classNo_max_total_score()))
    print("%s语文学科平均分是:%s" % (c.get_grade_class_name(), c.get_classNo_chinese_avg_score()))
    print("%s数学学科平均分是:%s" % (c.get_grade_class_name(), c.get_classNo_math_avg_score()))