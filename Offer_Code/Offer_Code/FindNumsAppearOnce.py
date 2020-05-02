# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 8:43
# @Author  : Shajiu
# @FileName: FindNumsAppearOnce.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
    一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""
class Solution:
    def FindNumsAppearOnce(self,array):
        tmp=[]
        for v in array:
            if array.count(v)==1:
                tmp.append(v)
        return tmp


array=[1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11]
if __name__ == '__main__':
    result=Solution()
    print(result.FindNumsAppearOnce(array))
