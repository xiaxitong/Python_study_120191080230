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
'''
1 将“网络编程”章节中课件中的例子，在本机测试运行；
'''
from socket import *


def main():
    # 绑定端口信息
    udp_socket = socket(AF_INET, SOCK_DGRAM)

    local_addr = ('', 9999)

    udp_socket.bind(local_addr)
    # 接收数据
    recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
    # 打印显示接收到的数据
    print(recv_data)

    # print(recv_data[0].decode('gbk'))
    # print(recv_data[1])

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()






















