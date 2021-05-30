#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:10-3_SQLAlchemy.py
# author:16546
# datetime:2021/5/30 15:41
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import threading

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from db import Users

engine = create_engine("mysql+pymysql://root:wenhongsu@localhost:3306/tea_list", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

#这个定制的Session类将创建新的Session对象绑定到我们的数据库。
# 无论何时你需要与数据库连接，你实例化一个Session:
session = Session()

# ################ 添加 ################
# session.add_all([
#     Users(name="wupeiqi",age = "22"),
#     Users(name="alex",age = "33"),
#     Users(name="alice",age = "44"),
# ])
# session.commit()


# ################ 删除 ################

# session.query(Users).filter(Users.id > 1).delete()
# session.commit()

# ################ 修改 ################

# session.query(Users).filter(Users.id > 0).update({"name" : "099"})
# # session.query(Users).filter(Users.id > 0).update({Users.name: Users.name + "099"}, synchronize_session=False)
# # session.query(Users).filter(Users.id > 0).update({"age": Users.age + 1}, synchronize_session="evaluate")
# session.commit()

# ################ 查询 ################

#r1是一个对象
r1 = session.query(Users).all()
# r2 = session.query(Users.name.label('xx'), Users.age).all()
# r3 = session.query(Users).filter(Users.name == "alex").all()
# r4 = session.query(Users).filter_by(name='alex').all()
# r5 = session.query(Users).filter_by(name='alex').first()
# r6 = session.query(Users).filter(text("id<:value and name=:name")).params(value=224, name='fred').order_by(Users.id).all()
# r7 = session.query(Users).from_statement(text("SELECT * FROM users where name=:name")).params(name='ed').all()
for i in r1:
    print(i.id, i.name,i.age)


session.close()



















