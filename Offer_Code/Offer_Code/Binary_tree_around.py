# -*- coding: utf-8 -*-
# @Time    : 2020/4/24 17:03
# @Author  : Shajiu
# @FileName: Binary_tree_around.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    """返回从上往下每个节点的值列表"""
    def PrintFromTopToBottom(self,root):
        l=[]
        if not root:
            return []
        q=[root]
        while len(q):
            t=q.pop(0)
            l.append(t.val)
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
        return l