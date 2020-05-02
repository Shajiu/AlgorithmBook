# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 8:52
# @Author  : Shajiu
# @FileName: FindContinuousSequence.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
    小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
    但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
    没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,
    你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
"""
class Solution:
    def FindContinuousSequence(self, tsum):
        global m
        m=tsum
        array=[]
        for x in range(1,m):
            result=self.Sum(x)
            if result!=0 and result!=None:
                array.append(result)
        return array

    def Sum(self,x):
        sum = 0
        tmp = []
        for i in range(x,m):
            sum+=i
            tmp.append(i)
            if sum==m:
                return tmp
            elif sum>m:
                return 0

if __name__ == '__main__':
    result=Solution()
    print(result.FindContinuousSequence(3))
