# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 11:15
# @Author  : shajiu
# @FileName: Perfect Squares.py
# @Software: PyCharm

def generateSquares(n):
    squares=[]
    square=1
    diff=3
    while square<=n:
        squares.append(square)
        square+=diff
        diff+=2
    return squares

if __name__ == '__main__':
    result=generateSquares(10)
    print(result)