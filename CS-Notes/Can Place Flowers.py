# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 15:29
# @Author  : shajiu
# @FileName: Can Place Flowers.py
# @Software: PyCharm

def canPlaceFlowers(flowerbed,n):
    print(flowerbed,n)
    len_1=len(flowerbed)
    cnt_1=0
    i=0

    while i<len_1 and cnt_1<n:
        print(i)
        if flowerbed[i]==1:
            continue
        per=i
        if per==0:
            per=0
        else:
            flowerbed[i-1]
        next=i
        if next==len_1-1:
            next=0
        else:
            flowerbed[i+1]
        if per==0 and next==0:
            cnt_1+=1
            flowerbed[i]=1
        i+=1
        print(i)
    return cnt_1>=n

if __name__ == '__main__':
    canPlaceFlowers([1,0,0,0,1],1)



