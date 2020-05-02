# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 20:24
# @Author  : Shajiu
# @FileName: Sum_Solution.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
    求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
"""
class Solution:
    def Sum_Solution(self,n):
        sum=0
        if n<0:
            print("您输入的是非法数据！")
        elif n==0 or n==1:
            sum=1
        else:
            sum=self.Sum_Solution(n-1)+n
        return sum

if __name__ == '__main__':
    result=Solution()
    print(result.Sum_Solution(100))
