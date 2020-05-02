# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 9:33
# @Author  : shajiu
# @FileName: test37.py
# @Software: PyCharm
lower=int(input("输入区间最小值:\n"))
upper=int(input("输入区间最大值:\n"))
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)