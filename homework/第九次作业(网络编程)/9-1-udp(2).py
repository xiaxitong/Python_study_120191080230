#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:9-1-udp(2).py
# author:16546
# datetime:2021/5/18 15:28
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from socket import *
def maan():
    udp_socket = socket(AF_INET,SOCK_DGRAM)

    local_addr = ('',9999)

    udp_socket.bind(local_addr)

    #接收数据
    recv_data = udp_socket.recvfrom(1024)
    #打印数据
    print(recv_data[0].decode('gbk'))
    udp_socket.close()

if __name__ == "__main__":
    maan()






















