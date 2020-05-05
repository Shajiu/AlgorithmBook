# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 18:00
# @Author  : shajiu
# @FileName: Non-decreasing Array.py
# @Software: PyCharm
def chekPossibility(nums):
    cnt=0
    i=1
    for i in range(len(nums)):
        if i<len(nums) and cnt<2:
            if (nums[i]>=nums[i-1]):
                continue
            cnt+=1
            if i-2>=0 and nums[i-2]>nums[i]:
                nums[i]=nums[i-1]
            else:
                nums[i-1]=nums[i]
    print(cnt)
    return cnt<-1

if __name__ == '__main__':
    chekPossibility([4,2,3])