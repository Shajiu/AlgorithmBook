# -*- coding: utf-8 -*-
# @Time    : 2020/4/28 12:27
# @Author  : Shajiu
# @FileName: LeftRotateString.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
   汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令
   的运算结果。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列
   S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
"""
class Solution:
    def LeftRotateString(self,s,n):
        tmp=[]
        s=[v for v in s]
        if len(s)>=n:
            for v in range(n,len(s)):
                tmp.append(s[v])

            for v in range(n):
                tmp.append(s[v])
            tmp=''.join(tmp)
            return tmp
        else:
            return ""

if __name__ == '__main__':
    result=Solution()
    print(result.LeftRotateString("abcXYZdef",3))