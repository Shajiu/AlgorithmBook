# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 10:33
# @Author  : shajiu
# @FileName: Reverse Linked List.py
# @Software: PyCharm
def reverseList(head):
    if head==0 or head.next==0:
        return head
    next=head.next
    newHead=reverseList(next)
    next.next=head
    head.next=0
    return newHead

#头插法
def reverseList(head):
    newHead=[]
    while(head!=0):
        next=head.next
        head.next=newHead.next
        newHead.next=head
        head=next
    return newHead.next




