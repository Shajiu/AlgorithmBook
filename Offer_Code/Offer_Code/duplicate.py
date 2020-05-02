# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 7:31
# @Author  : Shajiu
# @FileName: duplicate.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
   # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]   函数返回True/False
"""
class Solution:
    def duplicate(self,numbers, duplication):
        flag=False
        for v in numbers:
            if numbers.count(v)>1:
                duplication[0]=v
                flag = True
                break
        return flag

if __name__ == '__main__':
    result=Solution()
    print(result.duplicate([2,1,3,0,4],[0]))


"""第二种"""
import collections
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        flag=False
        c=collections.Counter(numbers)
        for k,v in c.items():
            if v>1:
                duplication[0]=k
                flag=True
                break
        return flag

if __name__ == '__main__':
    result=Solution()
    print(result.duplicate([1,2,3,4,3,5,5],[0]))




