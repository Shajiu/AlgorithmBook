# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 18:19
# @Author  : shajiu
# @FileName: test28.py
# @Software: PyCharm
def output(s,l):
    if l==0:
        return 0
    print(s[l-1])
    output(s,l-1)
s=input("input a string")
l=len(s)
output(s,l)
