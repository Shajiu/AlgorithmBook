# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 10:58
# @Author  : Shajiu
# @FileName: FindNumbersWithSum.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字
的和等于S，输出两个数的乘积最小的。
"""
class Solution:
    def FindNumbersWithSum(self,array,tsum):
        tmp=[]
        for v in array:
            for x in array:
                if v+x==tsum:
                    tmp.append((x,v))
        if len(tmp)>0:
            stm=[]
            for v in tmp:
                sum=1
                for i in list(v):
                    sum*=i
                stm.append(sum)
            p=stm
            stm.sort()
            t=p.index(stm[0])
            a=list(tmp[t])
            a.sort()
            return a
        else:
            return []

if __name__ == '__main__':
    result=Solution()
    print(result.FindNumbersWithSum([1,2,4,7,11,16],10))

