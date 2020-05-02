# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 21:40
# @Author  : Shajiu
# @FileName: Linked_list.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
功能： 单链表的初始化、赋值、输出
定义一个结点类    val   next
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList:
    def __init__(self):
        self.head=None

    """构建"""
    def initList(self, data):
        # 创建头结点
        self.head = ListNode(data[0])
        r=self.head
        p = self.head

        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next
        return r

    """打印"""
    def printlist(self,head):
        if head == None:
            return
        node = head
        while node != None:
            print(node.val,end='')
            node = node.next

if __name__ == '__main__':
    l=LinkList()
    data1 = [1, 2, 3]
    data2= [2, 4, 6]
    l1=l.initList(data1)

    l2=l.initList(data2)

    l.printlist(l1)