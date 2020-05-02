# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 17:36
# @Author  : Shajiu
# @FileName: Rectangle_cover.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目描述:矩形覆盖
       我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形
       无重叠地覆盖一个2*n的大矩形，总共有多少种方法？比如n=3时，2*3的矩形块有3种覆盖方法：
"""
class Solution:
    def rectCover(self, number):
        if number==1 or number==2:
            return number
        else:
            f1=1
            f2=2
            result=0
            for i in range(2,number):
                result=f1+f2
                f1=f2
                f2=result
            return result

if __name__ == '__main__':
    result=Solution()
    print(result.rectCover(3))
