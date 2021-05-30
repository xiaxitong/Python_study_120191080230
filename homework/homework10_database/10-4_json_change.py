#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:10-4_json_change.py
# author:16546
# datetime:2021/5/30 20:54
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
1 打印输出，年龄大于20岁的人员名单；
2 向列表中新增数据；
3 统计男生和女生的人数； 
'''
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="wenhongsu",
    database="json_list"
)
mycursor = mydb.cursor()
# 打印输出，年龄大于20岁的人员名单；
# sql = "SELECT * FROM sites WHERE age > 20"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

#向列表中新增数据；
# sql = "INSERT INTO sites (name, age, genda) VALUES (%s,%s, %s)"
# val = ("百度", 44, "未知")
# mycursor.execute(sql, val)
# mydb.commit()

#统计男生和女生的人数；
# sql = "SELECT * FROM sites WHERE genda = '男'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# boy = 0
# for x in myresult:
#     boy = boy + 1
# print(f'男生人数是：{boy}')

sql = "SELECT * FROM sites WHERE genda = '女'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
girl = 0
for x in myresult:
    girl = girl + 1
print(f'女生人数是：{girl}')

