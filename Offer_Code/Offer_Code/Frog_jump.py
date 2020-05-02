# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 17:30
# @Author  : Shajiu
# @FileName: Frog_jump.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目描述:  变态跳台阶
       一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
       求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
class Solution:
    def jumpFloorII(self, number):
        result=0
        if number<0:
            return 0
        elif number==0 or number==1 or number==2:
            return number
        else:
            n1=2
            for v in range(2,number):
                result=2*n1
                n1=result
            return result
if __name__ == '__main__':
    result=Solution()
    print(result.jumpFloorII(4))
