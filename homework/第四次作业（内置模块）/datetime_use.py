#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:datetime.py
# author:16546
# datetime:2021/4/14 16:24
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from datetime import datetime,timedelta
#timedelta类在datetime模块中

if __name__ == "__main__":
    date_str = input('输入日期：')
    date = datetime.strptime(date_str, '%Y.%m.%d')
    #将用户输入的字符串转换成datetime类型的数据，才能在程序中进行日期的操作，另外，格式符之间的符号与用户输入日期的间隔符
    #要一致

    cdate = date + timedelta(days = -43)
    #timedelta()用于将日期提前或延后，包含参数有：years，days，hours

    print(f'周数是：{cdate.isocalendar()[1]}\n星期是：{cdate.isocalendar()[2]}\n')
    #isocalendar()返回一个列表，元素为：[年份，周数，周几]