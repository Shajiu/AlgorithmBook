# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 8:51
# @Author  : shajiu
# @FileName: test72.py
# @Software: PyCharm
a=809
for i in range(10,100):
    b=i*a
    if b>=1000 and b<=9999 and 8*i>=10 and 8*i<99 and 9*i>=100 and 9*i<=999:
        print(i)
        print(809*i)