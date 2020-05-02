# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 9:19
# @Author  : Shajiu
# @FileName: dui_Push_Pop.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
class Solution:
    def __init__(self):
        self.stackA=[]
        self.stackB=[]
    def push(self,node):
        self.stackA.append(node)
    def pop(self):
        if not self.stackB:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        return self.stackB.pop()

if __name__ == '__main__':
    Solu=Solution()
