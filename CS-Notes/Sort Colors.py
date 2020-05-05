# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 18:19
# @Author  : shajiu
# @FileName: Sort Colors.py
# @Software: PyCharm

"""
按颜色进行排序
"""
def sortColors(nums):
    zero=-1
    one=0
    two=len(nums)
    while (one<two):
        if nums[one]==0:
            zero+=1
            swap(nums,zero,one)
            one+=1
        elif nums[one]==2:
            two-=1
            swap(nums,two,one)
        else:
            one+=1

def swap(nums,i,j):
    t=nums[i]
    nums[i]=nums[j]
    nums[j]=t
    print(nums)
if __name__ == '__main__':
    sortColors([2,0,2,1,1,0])