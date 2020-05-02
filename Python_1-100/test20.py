# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 17:19
# @Author  : shajiu
# @FileName: test20.py
# @Software: PyCharm
for i in range(ord("x"),ord("z")+1):
    for j in range(ord("x"),ord("z")+1):
        if i!=j:
            for k in range(ord("x"),ord("z")+1):
                if (i!=j):
                    for k in range(ord("x"),ord("z")+1):
                        if (i!=k) and (j!=k):
                            if (i!=ord("x")) and (k!=ord("x")) and (k!=ord("z")):
                                print("order is a --%s\t b--%s\tc--%s"%(chr(i),chr(j),chr(k)))