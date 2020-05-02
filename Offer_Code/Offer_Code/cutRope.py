# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 19:25
# @Author  : Shajiu
# @FileName: cutRope.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目；
     给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），
     每段绳子的长度记为k[0],k[1],...,k[m]。请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
     例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""
class Solution:
    def cutRope(self, number):
        # write code here
        if number == 1:return 1
        if number == 2:return 1
        if number == 3:return 2
        dp = [1]
        for i in range(2,number+1):
            maxs = i
            for j in range(1,i-1):
                tmp = dp[i-j-1]*j
                if tmp>maxs:
                    maxs = tmp
            dp.append(maxs)
        return dp[-1]


