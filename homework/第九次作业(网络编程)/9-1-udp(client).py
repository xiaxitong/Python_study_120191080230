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
import socket
import sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
s.connect((host,port))
msg = s.recv(1024)
s.close()
print(msg.decode('utf-8'))