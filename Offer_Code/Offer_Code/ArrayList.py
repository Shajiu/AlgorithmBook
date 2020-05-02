# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 16:21
# @Author  : shajiu
# @FileName: ArrayList.py
# @Software: PyCharm
"""
题目描述
       输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
"""
class Node():
    def __init__(self,elem,next_=None):
        self.elem=elem
        self.next=next_

    def reverseList(head):
        if head==None or head.next==None: #若链表为空或者仅一个值就直接返回
            return []
        pre=None
        next=None
        while(head!=None):
            next=head.next       #1
            head.next=pre        #2
            pre=head             #3
            head=next            #4

        return pre

if __name__ == '__main__':
    l1=Node(3)   #建立链表3->2->1->9->None
    l1.next=Node(2)
    l1.next.next=Node(1)
    l1.next.next.next=Node(9)

    l=Node.reverseList(l1)
    print (l.elem, l.next.elem, l.next.next.elem, l.next.next.next.elem)


#.....................第二种方法.......................................
class Solution:
    #返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailTohead(self,listNode):
        node=listNode
        stack=[]
        if node==Node:
            return []
        while node:
            stack.append(node.val)
            node=node.next
        stack.reverse()
        return stack

result=Solution()
if __name__ == '__main__':
    print(result.printListFromTailTohead({}))



