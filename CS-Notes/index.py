# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 11:29
# @Author  : shajiu
# @FileName: index.py
# @Software: PyCharm
def binarySearch(nums,key):
    l=0
    h=len(nums)-1
    while l<=h:
        m=l+(h-l)/2
        if nums[m]==key:
            return m
        elif nums[m]>key:
            h=m-1
        else:
            l=m+1
    return -1

if __name__ == '__main__':
    binarySearch([1,2,3,4,5],3)
