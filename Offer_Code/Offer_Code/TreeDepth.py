# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 20:50
# @Author  : Shajiu
# @FileName: TreeDepth.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu

"""
题目:
    输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
    最长路径的长度为树的深度。
"""
class Solution:
    def TreeDepth(self,pRoot):
        if pRoot==None:
            return 0
        left=self.TreeDepth(pRoot.left)
        right=self.TreeDepth(pRoot.right)
        return max(left,right)

