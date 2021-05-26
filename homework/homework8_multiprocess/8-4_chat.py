#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:8-4.py
# author:16546
# datetime:2021/5/19 17:05
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
from multiprocessing import Process, Queue
import os
import time
import random
'''
4 多进程通讯：
  编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；
'''

# 写数据进程执行的代码:
print('Process to write: %s' % os.getpid())
def write(q):
  for value in ['A', 'B', 'C']:
    print('Put %s to queue...' % value)
    q.put(value)
    time.sleep(random.random())

# 读数据进程执行的代码:
print('Process to read: %s' % os.getpid())
def read(q):
  while True:
    value = q.get()
    print('Get %s from queue.' % value)

if __name__ == '__main__': #父进程创建Queue， 并传给各个子进程：
  q = Queue()
  pw = Process(target = write, args = (q, ))
  pr = Process(target = read, args = (q, ))# 启动子进程pw， 写入:
  pw.start()# 启动子进程pr， 读取:
  pr.start()# 等待pw结束:
  pw.join()# pr进程里是死循环， 无法等待其结束， 只能强行终止:
  pr.terminate()