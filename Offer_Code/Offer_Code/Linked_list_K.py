# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 22:33
# @Author  : Shajiu
# @FileName: Linked_list_K.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目描述：
       输入一个链表，输出该链表中倒数第k个结点。
"""
class Solution:
    def FindKthTotail(self,head,k):
        if head==None or k<=0:
            return None

        p2=head
        p1=head
        while k>1:
            if p2.next!=None:
                p2=p2.next
                k-=1
            else:
                return None

            while p2.next!=None:
                p1=p1.next
                p2=p2.next
            return p1
                