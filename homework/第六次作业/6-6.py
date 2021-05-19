#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:6-6.py
# author:16546
# datetime:2021/5/19 17:22
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
def showInfo():
    print("-"*30)
    print("   学生管理系统 v1.0")
    print(" 1:添加学生的信息")
    print(" 2:删除学生的信息")
    print(" 3:修改的信息")
    print(" 4:查询学生的信息")
    print(" 5:遍历学生的信息")
    print(" 6:退出系统")
    print("-" * 30)


# 1.添加学生的信息
def addNewStu(studentsTemp):
    name = input("请输入姓名：")
    stuId = input("请输入学号：")
    age = input("请输入年龄：")

    # 2.判断是否能加这个学生：如果学生姓名已经存在报错提示；如果姓名不存在添加数据
    global students  # 声明students为全局变量

    # 2.1不允许学号重复：判断用户输入的学号和列表里面字典的id对应的值相等提示
    for i in students:
        if stuId == i['id']:
            print("该学号已经存在，请重新操作！！！")
            # return作用：退出当前函数，后面添加信息的代码不执行
            return

    # 2.2如果输入的姓名不存在，添加数据：准备空字典，字典新增数据，列表追加字典
    stuInfo = {}  # 2.2.1准备空字典

    # 2.2.2字典新增数据
    stuInfo['name'] = name  # 如果name存在赋值修改，如果name不存在则赋值新增“name”这个变量
    stuInfo['id'] = stuId
    stuInfo['age'] = age

    # 2.2.3列表追加字典数据
    studentsTemp.append(stuInfo)



# 2.删除学生的信息
def del_info():
    # 1.用户输入要删除的学生的学号
    del_name = input("请输入要删除的姓名：")

    # 2.判断学生是否存在：存在则删除：不存在提示
    # 2.1声明students为全局变量
    global students
    # 2.2遍历列表
    for i in students:
        # 2.3判断学生是否存在：存在执行删除（列表用面的学典）.break:这个系统不允许重名，删除了一个后面的不需要再遍历。不存在提示
        if del_name == i['name']:
            students.remove(i)
            break
    else:  # 循环正常结束
        print("该学生不存在")
    print(students)


# 3.修改学生的信息
def modify_info():
    # 1.用户输入想要修改的学生的姓名
    modify_name = input("请输入要修改的学生的姓名：")
    # 2.判断学生是否存在：存在修改学号：不存在，提示
    # 2.1声明students是全局变量
    global students
    # 2.2遍历列表，判断输入的姓名==字典['name']
    for i in students:
        if modify_name == i['name']:
            # 将stuId修改key值，并终止此循环
            i['id'] = input("请输入新的学号：")
            break
    else:
        # 学生不存在
        print("该学生不存在")
    # 3.打印students
    print(students)


# 4.查询学生的信息
def search_info():
    # 1.用户输入目标学生姓名
    search_name = input("请输入要查询的学生的姓名：")
    # 2.检查学生是否存在：存在打印这个学生的信息；不存在则提示
    # 2.1声明students为全局变量
    global students
    # 2.2遍历students，判断输入的学号是否存在
    for i in students:
        if search_name == i['name']:
            # 学员存在：打印信息并终止循环
            print("查询到的学生信息如下----------")
            print(f"学生的学号是{i['id']},学生的姓名是{i['name']},学生的年龄是{i['age']}")
            break
    else:
        # 学生不存在的提示
        print("对不起，您查询的学生不存在，请重试！")


# 5.遍历学生的信息
def print_all():
    # 1.打印提示字
    print('学号\t姓名\t年龄')

    # 2.打印所有学生的数据
    for i in students:
        print(f"{i['id']}\t{i['name']}\t{i['age']}")


students = []  # 等待存储所有学生信息
# 系统功能需要循环使用，直在用户输入6，才退出系统
while True:
    showInfo()  # 显示主界面
    key = int(input("请选择功能（序号）："))

    if key == 1:
        addNewStu(students)
    elif key == 2:
        del_info()
    elif key == 3:
        modify_info()
    elif key == 4:
        search_info()
    elif key == 5:
        print_all()
    elif key == 6:
        exit_flag = input("您确定要退出吗？yes/no\n")
        if exit_flag == 'yes':
            break
    else:
        print("输入有误，请重新输入!")