# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 9:32
# @Author  : Shajiu
# @FileName: TreeNode_Soluton.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
class Solution:
    def Mirror(self,root):

        """当传入的内容为空则结束"""
        if root==None:
            return 0

        """只有它的两个子节点同时为空时则不换位置否则为换位置"""
        if root.left==None and root.right==None:
            return 0

        """左右换位操作"""
        temp=root.left
        root.left=root.right
        root.right=temp

        """左节点作为新的根节点进行递归"""
        if(root.left!=None):
            self.Mirror(root.left)

        """右节点作为新的根节点"""
        if(root.right!=None):
            self.Mirror(root.right)




