# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 21:20
# @Author  : Shajiu
# @FileName: A+B_substructure.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
   输入两棵二叉树A，B，判断B是不是A的子结构。
   （ps：我们约定空树不是任意一个树的子结构）
"""
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution:
    def HasSubtree(self,pRoot1,pRoot2):

        if not pRoot1 or not pRoot2:
            return False

        return self.doesTree1HaveTree2(pRoot1,pRoot2) or \
               self.HasSubtree(pRoot1.left,pRoot2) or \
               self.HasSubtree(pRoot1.right,pRoot2)


    def doesTree1HaveTree2(self,pRoot1,pRoot2):
        """
        如果Tree2已经遍历完了都能对应上，返回true
        :param pRoot1:
        :param pRoot2:
        :return:
        """
        if not pRoot2:
            return True
        """如果Tree2还没有遍历完，Tree1却遍历完了。返回False"""
        if not pRoot1 or pRoot1.val!=pRoot2.val:
            return False
        """如果其中一个点没有对应上、返回False"""
        return self.doesTree1HaveTree2(pRoot1.left,pRoot2.left) and self.doesTree1HaveTree2(pRoot1.right,pRoot2.right)
