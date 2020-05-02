# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 20:59
# @Author  : Shajiu
# @FileName: Add.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
    写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
"""
class Solution:
    def Add(self,num1, num2):
        s=[]
        s.append(num1)
        s.append(num2)
        return sum(s)

if __name__ == '__main__':
    result=Solution()
    print(result.Add(10,20))
