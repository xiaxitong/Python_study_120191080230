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
