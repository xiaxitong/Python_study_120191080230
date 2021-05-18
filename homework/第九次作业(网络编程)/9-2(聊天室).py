#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:9-2(聊天室).py
# author:16546
# datetime:2021/5/18 20:21
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

def do_list():
    #创建一个udp套接字
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    dest_addr = ('192.168.1.111',8888)
#域名不能有空格
    send_data = input("请输入要发送的数据：")

    udp_socket.sendto(send_data.encode('utf-8'),dest_addr)

    udp_socket.close()

if __name__ == "__main__":
    while True:
       do_list()
       maan()
















