# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 14:42
# @Author  : shajiu
# @FileName: Merge Sorted Array.py
# @Software: PyCharm
def merge(nums1,m,nums2,n):
    print(nums1,nums2,m,n)
    index1=m-1
    index2=n-1
    indexMerge=m+n-1
    while index1>=0 or index2>=0:
        if index1<0:
            indexMerge-=1
            index1-=1
            nums1[indexMerge]=nums2[index1]
        elif index2<0:
            indexMerge-=1
            index1-=1
            nums1[indexMerge]=nums1[index1]
        elif nums1[index1]>nums2[index2]:
            indexMerge-=1
            index1-=1
            nums1[indexMerge]=nums1[index1]
        else:
            indexMerge-=1
            index2-=1
            nums1[indexMerge]=nums2[index2]
    print("测试结束！！！",nums1)
nums1 =[1,2,3,0,0,0]
m = 3
nums2 =[2,5,6]
n = 3
if __name__ == '__main__':
    merge(nums1,m,nums2,n)