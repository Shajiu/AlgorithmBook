# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 17:47
# @Author  : shajiu
# @FileName: test26.py
# @Software: PyCharm
"""
求1+2!+3!+...+20!的和
"""
sum2=0
for i in range(1,21):
    sum1=1
    print("-------")
    for j in range(1,i+1):
        print(j)
        sum1*=j
    sum2+=sum1
print("sum=",sum2)
