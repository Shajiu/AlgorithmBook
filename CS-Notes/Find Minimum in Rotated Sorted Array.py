# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 16:57
# @Author  : shajiu
# @FileName: Find Minimum in Rotated Sorted Array.py
# @Software: PyCharm


def findMin(nums):
    l=0
    h=len(nums)-1
    while l<h:
        m=int(l+(h-l)/2)
        if nums[m]<=nums[h]:
            h=m
        else:
            l=m+1
    return nums[l]

if __name__ == '__main__':
    result=findMin([3,4,5,1,2])
    print(result)