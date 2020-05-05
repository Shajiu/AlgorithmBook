# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 16:40
# @Author  : shajiu
# @FileName: Is Subsequence.py
# @Software: PyCharm
def isSubsequence(s,t):
    index=-1
    for i in range(len(s)):
        if s[i] not in t:
            index=1
        else:
            index=0
    if index==1:
        print("不在")
    else:
        print("在")

if __name__ == '__main__':
    s="abci"
    t="ahbgdc"
    isSubsequence(s,t)