#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:pickle模块.py
# author:16546
# datetime:2021/4/11 16:29
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import pickle
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

# 使用pickle模块将数据对象保存到文件
data1 = {'a': ['张三','120','2班'],
         'b': ['李四','121','2班'],
         'c': ['奥卡福','122','2班'],
         'd': ['阿富汗','123','2班'],
         'e': ['法规','124','2班']}


with open('data.pkl','wb') as output:
    pickle.dump(data1, output)
#填入数据到文件中
#.pkl文件是python保存文件的一种格式，如果直接打开会显示一堆序列化的东西，要用rb类型打开
#rb类型用于读取二进制文件


#重构文件对象
# with open('data.pkl','rb') as f:
#     print(pickle.load(f))
# #输出文件数据
#
# import pprint, pickle
#
# #使用pickle模块从文件中重构python对象
# pkl_file = open('data.pkl', 'rb')
#
# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)
#
# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)
#
# #!/usr/bin/python3
# pkl_file.close()