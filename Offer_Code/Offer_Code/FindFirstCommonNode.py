# -*- coding: utf-8 -*-
# @Time    : 2020/4/27 16:21
# @Author  : Shajiu
# @FileName: FindFirstCommonNode.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
    输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，
    所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
"""
class Listnode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def FindFirstCommonNode(self,pHead1,pHead2):
        p1=pHead1
        while p1:
            p2=pHead2
            while p2:
                if p1==p2:
                    return p1
                p2=p2.next
            p1=p1.next
        return None

