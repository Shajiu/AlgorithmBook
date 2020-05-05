# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 17:25
# @Author  : shajiu
# @FileName: Find First and Last Position of Element in Sorted Array.py
# @Software: PyCharm

import math
def searchRange(nums,target):
    first=fidFirst(nums,target)
    last=fidFirst(nums,target+1)-1

    if first==len(nums) and nums[first]!=target:
        return {-1,-1}
    else:
        return {first,math.max(first,last)}


def fidFirst(nums,target):
    l=0
    h=len(nums)
    while l<h:
        m=int(l+(h-1)/2)
        print(m)
        if nums[m]>=target:
            h=m
        else:
            l=m+1
    print(l)
    return l

if __name__ == '__main__':
    searchRange([5,7,7,8,8,10],8)

