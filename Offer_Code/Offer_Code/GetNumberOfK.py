# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 17:10
# @Author  : Shajiu
# @FileName: GetNumberOfK.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
    统计一个数字在排序数组中出现的次数。
"""
class Solution:
    def GetNumberOfK(self, data, k):
        return data.count(k)

data=[1,2,3,4,5,6,6,6,6,6,6,7,8,9,9]
k=6
if __name__ == '__main__':
    result=Solution()
    print(result.GetNumberOfK(data,k))
