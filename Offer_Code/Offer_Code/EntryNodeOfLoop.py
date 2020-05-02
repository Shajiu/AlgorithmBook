# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 11:44
# @Author  : Shajiu
# @FileName: EntryNodeOfLoop.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
    给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""
class Solution:
    def EntryNodeOfLoop(self,pHead):
        timeList=[]
        p=pHead
        while p:
            if p in timeList:
                return p
            else:
                timeList.append(p)
            p=p.next

