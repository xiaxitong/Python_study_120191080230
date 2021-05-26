#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:8-1.py
# author:16546
# datetime:2021/5/19 15:45
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import threading
import time
'''
1  有100个同学的分数：数据请用随机函数生成；
     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
     B 利用线程池来实现；
'''
def worker():
    global count
    while True:
        lock.acquire()	#加锁
        count += 1
        print(threading.current_thread(),count)
        lock.release()	#操作完成后释放锁
        if count >= 99:
            break
        time.sleep(1)
    print(1)

def main():
    threads = []
    for i in range(2):	#控制线程的数量
        t = threading.Thread(target=worker,args=())
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()	#将线程加入到主线程中

if __name__ == '__main__':
    lock = threading.Lock()
    count = 0
    main()






















