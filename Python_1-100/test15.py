# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 11:46
# @Author  : shajiu
# @FileName: test15.py
# @Software: PyCharm
Tn=0
Sn=[]
n=int(input("n="))
a=int(input("a="))
for count in range(n):
    Tn=Tn+a
    a=a*10
    Sn.append(Tn)
    print(Tn)

sum=0
for i in Sn:
    sum+=i
print("计算和为:",sum)

