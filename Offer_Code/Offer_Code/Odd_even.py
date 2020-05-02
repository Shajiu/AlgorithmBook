# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 21:26
# @Author  : Shajiu
# @FileName: Odd_even.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
描述:
    输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
    所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""
class Solution:
    def reOrderArray(self, array):
        odd=[]
        even=[]
        for v in array:
            if v%2==0:
                odd.append(v)
            else:
                even.append(v)
        even.extend(odd)
        return even

if __name__ == '__main__':
    array=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    result=Solution()
    print(result.reOrderArray(array))
