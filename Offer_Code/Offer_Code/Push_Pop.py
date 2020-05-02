# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 9:27
# @Author  : Shajiu
# @FileName: Push_Pop.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目描述:
       用两个栈来实现一个队列，完成队列的Push和Pop操作。
       队列中的元素为int类型。
"""
class Solution:
    def __index__(self):
        self.stackA=[]
        self.stackB=[]
    def push(self,node):
        self.stackA.append(node)
    # write code here
        pass
    def pop(self):
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop(0))
        return self.stackB.pop()