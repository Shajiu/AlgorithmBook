# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 21:24
# @Author  : shajiu
# @FileName: test03.py
# @Software: PyCharm
for i in range(1,85):
    if 168%i==0:
        j=168/i
        if i>j and (i+j)%2==0 and (i - j) % 2 == 0:
            m=(i+j)/2
            n=(i-j)/2
            x=n*n-100
            print(x)