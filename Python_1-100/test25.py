# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 17:33
# @Author  : shajiu
# @FileName: test25.py
# @Software: PyCharm
"""
有一分数序列：2/1，3/2，5/3，
8/5，13/8，21/13...求出这个数列的前20项之和。
"""
x1=2
x2=1
sum=0
for i in range(20):
    sum+=x1/x2
    x3=x1
    x1=x1+x2
    x2=x3
print(sum)
