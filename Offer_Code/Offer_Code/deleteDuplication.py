# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 11:55
# @Author  : Shajiu
# @FileName: deleteDuplication.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
   在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，
   返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""
class Listnode:
    def __init__(self,x):
        self.val=x
        self.next=None
class Solution:
    def deleteDuplication(self,pHead):
        result=Listnode(0)
        res=result
        result.next=pHead
        tmp=pHead
        while tmp and tmp.next:
            if tmp.val==tmp.next.val:
                while tmp.next and tmp.val==tmp.next.val:
                    tmp=tmp.next
            else:
                res.next=tmp
                res=res.next
            tmp=tmp.next
        res.next=tmp
        return result.next
if __name__ == '__main__':
    result=Solution()
    print(result.deleteDuplication([1,2,3,3,4,4,5]))

