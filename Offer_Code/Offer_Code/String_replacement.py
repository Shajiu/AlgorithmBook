# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 10:31
# @Author  : shajiu
# @FileName: String_replacement.py
# @Software: PyCharm
"""
题目描述:
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串
为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
"""
class Solution:
    def replaceSpace(self,s):
        s=s.replace(" ","%20")
        return s
S=Solution()
tmp="We Are Happy"
if __name__ == '__main__':
    print("结果为:",S.replaceSpace(tmp))


""""
注明：
以下为存在多个空格时也会将把所有的空格都替换为一个字符串
使用到的是正则表达式
"""
import re
s="We Are Happy"
a=re.sub(" +","%20",s)
print("测试段:",a)