#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_set.py
# author:16546
# datetime:2021/3/14 20:13
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
if __name__ == "__main__":
    set1 = {'apple', 'pear', 'orange'}
    set2 = set(('a', 'b', 'c'))
    set2.add('d')
    print(set1)
    print(set2)
    set1.remove('apple')
    print(f'集合二的元素个数为：{len(set2)}')
    set2.clear()
    print(set2)
    print(f'{"apple" in set1}')
