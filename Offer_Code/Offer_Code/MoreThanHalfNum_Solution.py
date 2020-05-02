# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 15:09
# @Author  : Shajiu
# @FileName: MoreThanHalfNum_Solution.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组
    {1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
    如果不存在则输出0。
"""
class Solution:
    def MoreThanHalfNum_Solution(self,numbers):
        dic={}
        for i in numbers:
            i=str(i)
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        dic=sorted(dic.items(), key=lambda x: x[1], reverse=False)
        num=int(dic[-1][-1])
        if num>len(numbers)/2:
            result=[k for (k,v) in dic if v==num]
            return int(''.join(result))
        else:
            return 0

if __name__ == '__main__':
    result=Solution()
    print(result.MoreThanHalfNum_Solution([4,2,1,4,2,4]))