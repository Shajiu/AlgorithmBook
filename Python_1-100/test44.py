# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 20:02
# @Author  : shajiu
# @FileName: test44.py
# @Software: PyCharm
num=2
def autofunc():
    num=1
    print("internal block num=%d"%num)
    num+=1
for i in range(3):
    print("The num=%d"%num)
    num+=1
    autofunc()
