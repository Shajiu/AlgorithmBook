# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 16:31
# @Author  : Shajiu
# @FileName: Take_the_first_few.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
    输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，
    则最小的4个数字是1,2,3,4,。
"""
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        tinput=list(tinput)
        tinput.sort()
        if k<=len(tinput):
            return tinput[:k]
        else:
            return []

if __name__ == '__main__':
    result=Solution()
    print(result.GetLeastNumbers_Solution((4,5,1,6,2,7,3,8),4))