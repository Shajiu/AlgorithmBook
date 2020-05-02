# -*- coding: utf-8 -*-
# @Time    : 2020/4/29 21:10
# @Author  : Shajiu
# @FileName: StrToInt.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
    将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
"""
class Solution:
    def StrToInt(self,s):
        if len(s)==0:
            return 0
        else:
            if s[0]>"9" or s[0]<"9":
                a=0
            else:
                a=int(s[0])*10**(len(s)-1)
            if len(s)>1:
                for i in range(1,len(s)):
                    if s[i]>="0" and s[i]<="9":
                        a=a+int(s[i])*10**(len(s)-1-i)
                    else:
                        return 0
                if s[0]=="+":
                    return a
                if s[0]=='-':
                    return -a
                return a




if __name__ == '__main__':
    result=Solution()
    print(result.StrToInt("b"))

