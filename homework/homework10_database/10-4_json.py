#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:10-4_jason.py
# author:16546
# datetime:2021/5/30 17:30
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''

'''
import json
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="wenhongsu",
    database="json_list"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE sites (name VARCHAR(255), age VARCHAR(255), genda VARCHAR(255))")
# sql = 'insert into tbl values ("%s")' % obj['id'] #这里注意编码，要转成数据库的编码格式
json_str = [
    {
        "name": "Frank",
        "age": 15,
        "genda": "男"
    },
    {
        "name": "tracy",
        "age": 20,
        "genda": "女"
    },
    {
        "name": "cythia",
        "age": 21,
        "genda": "女"
    },
    {
        "name": "王五",
        "age": 19,
        "genda": "男"
    },
    {
        "name": "jackie",
        "age": 19,
        "genda": "男"
    }
]
for i in json_str:
    val = []
    val.append((i['name'],i['age'],i['genda']))
    sql = "INSERT INTO sites (name, age, genda) VALUES (%s, %s, %s)"
    mycursor.executemany(sql, val)
    mydb.commit()
print("记录插入成功。")




