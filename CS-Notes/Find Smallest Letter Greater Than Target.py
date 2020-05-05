# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 14:41
# @Author  : shajiu
# @FileName: Find Smallest Letter Greater Than Target.py
# @Software: PyCharm
def nexGreatesLetter(letters,target):
    n=len(letters)
    l=0
    h=n-1
    print(h)
    # while l<=h:
    #     m=l+(h-1)/2
    #     if letters[m]<=target:
    #         l=m+1
    #     else:
    #         h=m-1
    # if l<n:
    #     return letters[1]
    # else:
    #     return letters[0]

if __name__ == '__main__':
    nexGreatesLetter(["c", "f", "j"],"d")