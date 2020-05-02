# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 17:59
# @Author  : shajiu
# @FileName: test27.py
# @Software: PyCharm
"""
利用递归方法求5!
"""
sum=0
def fact(j):
    if j==0:
        sum=1
    else:
        sum=j*fact(j-1)
    return sum
print(fact(5))