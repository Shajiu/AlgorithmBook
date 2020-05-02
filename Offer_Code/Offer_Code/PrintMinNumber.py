# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 18:18
# @Author  : Shajiu
# @FileName: PrintMinNumber.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
   输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
   例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
"""
from itertools import combinations,permutations
class Solution:
    def PrintMinNumber(self,numbers):
        if len(numbers)>0:
            tmp = list(permutations(numbers, len(numbers)))
            array = []
            for v in tmp:
                array.append(int(''.join([str(x) for x in v])))
            array.sort()
            return array[0]
        else:
            return ''


if __name__ == '__main__':
    result=Solution()
    print(result.PrintMinNumber([3,32,321]))
