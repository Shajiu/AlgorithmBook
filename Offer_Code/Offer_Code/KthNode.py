# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 18:18
# @Author  : Shajiu
# @FileName: KthNode.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
    给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）
    中，按结点数值大小顺序第三小结点的值为4。
"""
class Solution:
    def KthNode(self,pRoot,k):
        global result
        result=[]
        self.midnode(pRoot)
        if k<=0 or len(result)<k:
            return None
        else:
            return result[k-1]

    def midnode(self,root):
        if not root:
            return None
        self.midnode(root.left)
        result.append(root)
        self.midnode(root.right)


if __name__ == '__main__':
    result=Solution()
    print(result.KthNode())