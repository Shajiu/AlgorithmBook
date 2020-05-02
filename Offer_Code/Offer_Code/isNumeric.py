# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 8:12
# @Author  : Shajiu
# @FileName: isNumeric.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
    请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"
    和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""
class Solution:
    def isNumeric(self,s):
        try:
            p = float(s)
            return True
        except:
            return False
if __name__ == '__main__':
    result=Solution()
    print(result.isNumeric('5e2'))
