# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 14:32
# @Author  : Shajiu
# @FileName: GetNext.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
    给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，
    树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""
class Solution:
    def GetNext(self,pNode):
        if pNode.right:
            cur=pNode.right
            while cur.left:
                cur=cur.left
            return cur
        else:
            p=pNode.next
            if not p:
                return None
            else:
                if p.left==pNode:
                    return p
                else:
                    cur=pNode
                    while p and p.right==cur:
                        cur=p
                        p=cur.next
                    return p

if __name__ == '__main__':
    result=Solution()
    print(result.GetNext(0))

