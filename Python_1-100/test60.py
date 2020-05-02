# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 16:34
# @Author  : shajiu
# @FileName: test60.py
# @Software: PyCharm
if __name__ == '__main__':
    nma=50
    n=int(input("请您输入总人数:"))
    num=[]
    for i in range(n):
        num.append(i+1)

    i=0
    k=0
    m=0

    while m<n-1:
        if num[i]!=0:
            k+=1
        if k==3:
            num[i]=0
            k=0
            m+=1
        i+=1

        if i ==n:i=0
    i=0
    while num[i]==0:i+=1
    print(num[i])
