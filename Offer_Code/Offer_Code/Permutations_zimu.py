# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 9:37
# @Author  : Shajiu
# @FileName: Permutations_zimu.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
    输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c
    所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""
from itertools import combinations,permutations
import re
class Solution:
    def Permutation(self, ss):
        if len(ss)>=1:
            ss=re.sub(' +','',ss)
            val=[s for s in ss.strip(' ')]
            result=permutations(val,len(val))
            result=list(result)
            result_l=[]
            for v in result:
                tmp=''.join(v)
                result_l.append(tmp)
            return list(set(result_l))
        else:
            return []

if __name__ == '__main__':
    result=Solution()
    print(result.Permutation('a'))



"""第二种方法"""
import itertools
class Solution:
    def Permutation(self,ss):
        if not ss:
            return []
        #return sorted(list(set(map(''.join,itertools.permutaions(ss)))))

if __name__ == '__main__':
    result=Solution()
    print(result.Permutation('aa'))

"""
第三种方法
"""
class Solution:
    def Permutation(self,ss):
        if not len(ss):
            return []
        if len(ss)==1:
            return list(ss)
        charList=list(ss)
        charList.sort()
        pStr=[]
        for i in range(len(charList)):
            if i>0 and charList[i]==charList[i-1]:
                continue
            temp=self.Permutation(ss[:i]+ss[i+1:])
            for j in temp:
                pStr.append(charList[i]+j)
        return pStr

if __name__ == '__main__':
    result=Solution()
    print(result.Permutation('abc'))