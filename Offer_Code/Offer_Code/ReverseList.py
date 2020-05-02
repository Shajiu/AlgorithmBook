# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 15:35
# @Author  : Shajiu
# @FileName: ReverseList.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
   输入一个链表，反转链表后，输出新链表的表头
"""
class Solution:
    def ReverseList(self, pHead):
        if(pHead==None):
            return None
        pre=None
        next=None
        while pHead!=None:
            next=pHead.next   #让next引用指向pHead下一个结点。
            pHead.next=pre    #pre始终指向当前pHead的前一个节点，这样可以反转节点了
            pre=pHead
            pHead=next
        return pre
