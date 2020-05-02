# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 11:02
# @Author  : shajiu
# @FileName: test79.py
# @Software: PyCharm
a=int(input("输入四个数字:\n"))
aa=[]
aa.append(a%10)
aa.append(a%100/10)
aa.append(a%1000/100)
aa.append(a/1000)

for i in range(4):
    aa[i]+=5
    aa[i]%=10
for i in range(2):
    aa[i],aa[3-i]=aa[3-i],aa[i]

