# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 11:41
# @Author  : Shajiu
# @FileName: Jump_the_stairs.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
描述:
    一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
    （先后次序不同算不同的结果）。
"""
class Solution:
    def jumpFloor(self, number):
        result=0
        if number<0:
            return 0
        elif number==0 or number==1 or number==2:
            return number
        else:
            n1=1
            n2=2
            for x in range(2,number):
                result=n1+n2
                n1=n2
                n2=result
        return result
if __name__ == '__main__':
    result=Solution()
    result=result.jumpFloor(4)
    print(result)