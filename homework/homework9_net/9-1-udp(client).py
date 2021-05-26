#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:9-1-udp(client).py
# author:16546
# datetime:2021/5/18 15:43
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
1 将“网络编程”章节中课件中的例子，在本机测试运行；
'''
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))

# 接收小于 1024 字节的数据
msg = s.recv(1024)

s.close()

print (msg.decode('utf-8'))