# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 16:00
# @Author  : shajiu
# @FileName: Single Element in a Sorted Array.py
# @Software: PyCharm
def singleNonDuplicate(nums):
    l=0
    h=len(nums)-1
    while(l<h):
        m=l+(h-1)/2
        if m%2==1:
            m-=1
        if nums[m]==nums[m+1]:
            l=m+2
        else:
            h=m
    return nums[l]

if __name__ == '__main__':
    singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
