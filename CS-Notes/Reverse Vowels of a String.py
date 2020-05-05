# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 18:21
# @Author  : shajiu
# @FileName: Reverse Vowels of a String.py
# @Software: PyCharm
"""
反转字符串中的元音字符
"""

input  = "leetcode"
output ="leotcede"
aslist=['a','e','i','o','u','A','E','I','O','U']

def reverseVowels(s):
    if s==0:
        return 0
    i=0
    j=len(s)-1
    result=[]
    while i<=j:
         ci=s[i]
         cj=s[j]
         i+=1
         if ci not in aslist:
             result[i]=ci
             i+=1
             print(ci)

         elif cj not in aslist:
             result[j]=cj
             j-=1

         else:
             i+=1
             result[i]=cj
             j-=1
             result[j]=ci

    return result

if __name__ == '__main__':
    reverseVowels("leetcode")


