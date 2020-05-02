# -*- coding: utf-8 -*-
# @Time    : 2020/4/22 21:39
# @Author  : Shajiu
# @FileName: Pop-up-order.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
    假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压
    栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
    （注意：这两个序列的长度是相等的）
"""
class Solution:
    def IsPopOrder(self,pushv,popv):
        if not pushv or len(pushv)!=len(popv):
            return False
        stack=[]
        for i in pushv:
            stack.append(i)
            while len(stack) and stack[-1]==popv[0]:
                stack.pop()
                popv.pop(0)
            if len(stack):
                return False
            return True
