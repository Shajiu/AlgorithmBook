# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 18:20
# @Author  : Shajiu
# @FileName: Binary.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：二进制数中1的个数
    输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""
class Solution:
    def NumberOf1(self, n):
        return sum([(n>>i & 1) for i in range(0,32)])

if __name__ == '__main__':
    result=Solution()
    print(result.NumberOf1(10))
