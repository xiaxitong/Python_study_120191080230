#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:9-1-udp(server).py
# author:16546
# datetime:2021/5/18 15:36
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import socket
import sys

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#获取本地主机名
host = socket.gethostname()
port = 9999
#绑定端口号
serversocket.bind((host,port))
#设置最大连接数
serversocket.listen(5)
while True:
    #建立客户端连接
    clientsocket,addr = serversocket.accept()
    print(str(addr))
    msg = '欢迎'+'\n'
    clientsocket.sendto(msg.encode('utf-8'))
    clientsocket.close()