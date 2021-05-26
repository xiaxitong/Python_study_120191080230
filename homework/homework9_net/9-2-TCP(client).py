#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:9-2-TCP.py
# author:16546
# datetime:2021/5/18 19:40
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
'''
编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；
'''
#TCP协议建立的是双向通道，但是客户端和服务端如何协调通信要根据具体的协议来定。

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#AF_INET指定使用IPv4。SOCK_STREAM指定使用面向流的TCP协议

s.connect(('www.baidu.com',80))
#建立连接
#新浪网站的IP地址可以通过域名自动转换，而各种不同的服务有着固定的标准端口号，提供网页服务的是80端口。

s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
#发送请求，要求返回新浪首页的内容
####  注意上面语句中空格的使用

buffer = []

while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
s.close()

#将接收到的HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件
header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
with open('baidu.html', 'wb') as f:
    f.write(html)


























