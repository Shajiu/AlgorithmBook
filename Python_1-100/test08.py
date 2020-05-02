# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 9:48
# @Author  : shajiu
# @FileName: test08.py
# @Software: PyCharm
"""乘法口诀"""
for i in range(1,10):
    print()
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,i*j))