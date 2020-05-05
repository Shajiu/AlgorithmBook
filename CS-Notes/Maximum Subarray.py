# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 8:28
# @Author  : shajiu
# @FileName: Maximum Subarray.py
# @Software: PyCharm
def partitionLabels(s):
    lastIndexsOfChar=[]
    for i in range(len(s)):
        lastIndexsOfChar[s[i]]=i
    firstIndex=0
    while firstIndex<len(s):
        lastIndex=firstIndex
        i=firstIndex
