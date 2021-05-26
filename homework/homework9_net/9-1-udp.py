#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:9-1-udp.py
# author:16546
# datetime:2021/5/18 14:57
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
1 将“网络编程”章节中课件中的例子，在本机测试运行；
'''
import socket
def do_list():
    #创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    dest_addr = ('192.168.1.108',8888)
#域名不能有空格
    send_data = input("请输入要发送的数据：")

    udp_socket.sendto(send_data.encode('utf-8'),dest_addr)

    udp_socket.close()

if __name__ == '__main__':
    do_list()



























