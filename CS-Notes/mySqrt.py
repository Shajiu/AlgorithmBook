# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 12:05
# @Author  : shajiu
# @FileName: mySqrt.py
# @Software: PyCharm
def mySqrt(x):
    if x<=1:
        return x
    l=1
    h=x
    while (l<=h):
        mid=l+(h-l)/2
        sqrt=x/mid
        if(sqrt==mid):
            return mid
        elif mid>sqrt:
            h-mid-1
        else:
            l=mid+1
        print(h)
    return h

if __name__ == '__main__':
    mySqrt(8)