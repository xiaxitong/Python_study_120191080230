#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:10-2_PyMySQL.py
# author:16546
# datetime:2021/5/29 16:45
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
# import mysql.connector
#
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="wenhongsu",
#     database="stu_list"
# )
# mycursor = mydb.cursor()
import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="wenhongsu", database="stu_list")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

'''
增加数据
'''
# sql = """INSERT INTO sites(name,
#          sex, class, age)
#          VALUES ('Mac', '男', 'class 3', '33')"""
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 如果发生错误则回滚
#     db.rollback()

'''
查询数据
fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
'''
# sql = "SELECT * FROM sites \
#        WHERE age > 22"
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#          print(row)
# except:
#     print("Error: unable to fetch data")

'''
修改数据
'''
# sql = "UPDATE sites SET age = age + '1' WHERE SEX = '%s'" % ('男')
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 提交到数据库执行
#     db.commit()
# except:
#     # 发生错误时回滚
#     db.rollback()

'''
删除数据
'''
# SQL 删除语句
sql = "DELETE FROM sites WHERE age > '%s'" % ('40')
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()
# 关闭数据库连接
db.close()























