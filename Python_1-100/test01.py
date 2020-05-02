# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 18:45
# @Author  : shajiu
# @FileName: test01.py
# @Software: PyCharm
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i!=j) and (i!=k) and (j!=k):
                print(i,j,k)