#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:8-2.py
# author:16546
# datetime:2021/5/19 15:55
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import io
import sys
'''
1  有100个同学的分数：数据请用随机函数生成；
     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
     B 利用线程池来实现；

2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
   请查资料，Python的 requests库，如何判断一个网址可以访问；
提示 ：使用requests模块
   def getHtmlText(url):
    try:        # 网络连接有风险，异常处理很重要
        r = requests.get(url,timeout=30)    # 查一下这个方法的使用
        r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
         return "产生异常"
'''
def maan():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    filename = 'url_data.txt'
    with open(filename, 'r') as f:
        url = f.readlines()
    length = len(url)
    url_result_success=[]
    url_result_failed=[]
    for i in range(0,length):
        try:
            response = requests.get(url[i].strip(), verify=False, allow_redirects=True, timeout=5)
            #requests.get()用于请求目标网站，类型是一个HTTPresponse类型
            if response.status_code != 200:
                raise requests.RequestException(u"Status code error: {}".format(response.status_code))
        except requests.RequestException as e:
            url_result_failed.append(url[i])
            continue
        url_result_success.append(url[i])
    result_len1 = len(url_result_failed)
    result_len2= len(url_result_success)
    for i in range(0,result_len1):
        print (url_result_failed[i].strip()+"打开失败")
    print("   ")
    for j in range(0,result_len2):
	    print (url_result_success[j].strip()+"打开成功")

if __name__=='__main__':
    maan()
