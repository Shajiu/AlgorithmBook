# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 10:21
# @Author  : Shajiu
# @FileName: Matrix_clockwise.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
   输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，
   如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
   则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""
class Solution:
    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self,node):
        self.stack.append(node)
        if not self.min_stack or node<=self.min_stack[-1]:
            self.min_stack.append(node)

    def pop(self):
        if self.stack[-1]==self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]