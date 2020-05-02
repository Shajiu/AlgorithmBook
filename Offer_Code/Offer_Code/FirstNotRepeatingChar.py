# -*- coding: utf-8 -*-
# @Time    : 2020/4/26 8:05
# @Author  : Shajiu
# @FileName: FirstNotRepeatingChar.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
   在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
   并返回它的位置, 如果没有则返回 -1（需要区分大小写）
"""
class Solution:
    def FirstNotRepeatingChar(self,s):
        if s=="":
            return -1
        for i in s:
            if s.count(i)==1:
                return s.index(i)

txt="hellwoedwoehie daodew"
if __name__ == '__main__':
    result=Solution()
    print(result.FirstNotRepeatingChar(txt))