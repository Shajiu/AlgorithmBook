# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 17:50
# @Author  : Shajiu
# @FileName: NumberOf1Between1AndN_Solution.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目：
   求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中
   包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,
   并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""
class Solution:
    def NumberOf1Between1AndN_Solution(self,n):
        arry=[]
        for v in range(n+1):
            arry.append(str(v))
        arry=[v for v in ''.join(arry).strip()]
        print(arry)
        sum=0
        for v in arry:
            if "1" in v:
                sum+=1
        return sum

if __name__ == '__main__':
    result=Solution()
    print(result.NumberOf1Between1AndN_Solution(1))