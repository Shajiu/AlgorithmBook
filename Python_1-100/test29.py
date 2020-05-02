# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 18:28
# @Author  : shajiu
# @FileName: test29.py
# @Software: PyCharm
"""
递归的形式计算
"""
def aver(num):
    if num ==1:
        age=10
    else:
        age=aver(num-1)+2
    return age
print(aver(5))
