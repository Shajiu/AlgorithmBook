# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 20:53
# @Author  : Shajiu
# @FileName: exponent.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目描述:
       给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。保证base和exponent不同时为0
"""
class Solution:
    """底数、指数"""
    def Power(self,base,exponent):
        if exponent==0:
            return 1
        if base==0:
            return 0
        return pow(base,exponent)

if __name__ == '__main__':
    result=Solution()
    print(result.Power(2,3))