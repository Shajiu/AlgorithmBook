# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 8:22
# @Author  : Shajiu
# @FileName: IsBalanced_Solution.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
    输入一棵二叉树，判断该二叉树是否是平衡二叉树。在这里，我们只需要考虑其平衡性，
    不需要考虑其是不是排序二叉树
"""
class Solution:
    def IsBalanced_Solution(self,pRoot):
        if pRoot==None:
            return True
        left=self.Deep(pRoot.left)
        right=self.Deep(pRoot.right)
        diff=left-right
        if diff>1 or diff<-1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def Deep(self,pRoot):
        if pRoot==None:
            return 0
        left=self.Deep(pRoot.left)
        right=self.Deep(pRoot.right)
        if left>right:
            return left+1
        else:
            return right+1


