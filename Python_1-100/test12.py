# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 10:47
# @Author  : shajiu
# @FileName: test12.py
# @Software: PyCharm
for n in range(100,1000):
    i=n//100
    j=n//10%10
    k=n%10
    if n==i**3+j**3+k**3:
        print(n)