# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 15:28
# @Author  : Shajiu
# @FileName: Print.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:

"""
class Solution:
    def Print(self,pRoot):
        if pRoot is None:
            return []
        result=[]
        q=[pRoot]
        while q:
            q_tmp=q
            q=[]
            cur_row=[]
            while q_tmp:
                node=q_tmp.pop(0)
                cur_row.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(cur_row)
        return result


if __name__ == '__main__':
    res=Solution()
    print(res.Print())
