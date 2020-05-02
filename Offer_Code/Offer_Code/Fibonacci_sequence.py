# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 11:08
# @Author  : Shajiu
# @FileName: Fibonacci_sequence.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""

题目描述: 斐波那契数列----F(n)=F(n-1)+F(n-2)
      大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项
      （从0开始，第0项为0）。
n<=39
"""
class Solution:
    def Fibonacci(self,n):
        array=[1,1]
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            for i in range(2,n):
                tmp=array[i-1]+array[i-2]
                array.append(tmp)
        return array[n-1]

if __name__ == '__main__':
    result=Solution()
    print(result.Fibonacci(7))