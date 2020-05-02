# -*- coding: utf-8 -*-
# @Time    : 2020/4/30 21:35
# @Author  : Shajiu
# @FileName: match.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目；
    请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，
    而'*'表示它前面的字符可以出现任意次（包含0次）。 在本题中，匹配是指字符串的所有
    字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"
    和"ab*a"均不匹配
"""
class Solution:
    def match(self,s,pattern):
        if not pattern and not s:
            return True
        if not pattern and s:
            return False
        if len(pattern)>1 and pattern[1]=="*":
            if s and (pattern[0]==s[0] or pattern[0]=='.' and s):
                return self.match(s,pattern[2:]) or self.match(s[1:],pattern) or (self.match(s[1:],pattern[2:]))
            else:
                return self.match(s,pattern[2:])
        if s and (pattern[0]==s[0] or pattern[0]=='.' and s):
            return self.match(s[1:],pattern[1:])
        else:
            return False




if __name__ == '__main__':
    result=Solution()
    print(result.match(""))