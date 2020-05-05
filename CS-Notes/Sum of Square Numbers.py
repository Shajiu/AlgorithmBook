# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 17:47
# @Author  : shajiu
# @FileName: Sum of Square Numbers.py
# @Software: PyCharm

import math
#   两数平方和
def judgeSquareSum(target):
    if target<0:
        return 0
    i=0
    j=math.sqrt(target)
    print(0,i,j)
    while(i<=j):
        powSum=i*i+j*j
        if powSum==target:
            print("==")
            return 1
        elif powSum>target:
            print(">")
            j-=1
        else:
            i+=1

            print("<")
    return 0
if __name__ == '__main__':
    judgeSquareSum(5)