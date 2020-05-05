# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 11:52
# @Author  : shajiu
# @FileName: Valid Palindrome.py
# @Software: PyCharm
def validPalindrome(s):
    i=0
    j=len(s)-1
    while i < j:
        if s[i]!=s[j]:
            i+=1
            j-=1
            return isPalindrome(s,i,j-1),isPalindrome(s,i+1,j)
    return "yes"

def isPalindrome(s,i,j):
    while i<j:
        i+=1
        j-=1
        if s[i]!=s[j]:
            return "yes"
    return "no"

if __name__ == '__main__':
    validPalindrome("abca")