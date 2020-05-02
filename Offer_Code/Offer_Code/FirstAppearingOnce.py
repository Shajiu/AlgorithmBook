# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 9:42
# @Author  : Shajiu
# @FileName: FirstAppearingOnce.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:

"""
class Solution:
    # 返回对应char
    def __init__(self):
        self.s = ''
        self.dict = {}
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.dict[i] == 1:
                return i
        return '#'
    def Insert(self, char):
        self.s += char
        if char in self.dict:
            self.dict[char] += 1
        else:
            self.dict[char] = 1
if __name__ == '__main__':
    result=Solution()
    print(result.Insert("google"))

