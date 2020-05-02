# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 17:51
# @Author  : Shajiu
# @FileName: Serialize.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
    请实现两个函数，分别用来序列化和反序列化二叉树 二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式
    保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树遍历方式
    来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。
    二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树 例如，我们可以把一个只有根节点为1的
    二叉树序列化为"1,"，然后通过自己的函数来解析回这个二叉树
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        if root == None:
            return '#'

        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        root, index = self.Des(s.split(','), 0)
        return root

    def Des(self, s, index):
        if index == len(s):
            return root, index
        if s[index] == '#':
            return None, index + 1
        root = TreeNode(int(s[index]))

        index += 1

        root.left, index = self.Des(s, index)
        root.right, index = self.Des(s, index)

        return root, index