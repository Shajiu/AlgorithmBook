# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 8:44
# @Author  : shajiu
# @FileName: test49.py
# @Software: PyCharm
def exchange(a,b):
    a,b=b,a
    return (a,b)
if __name__ == '__main__':
    x=10
    y=20
    print("x=%d,y=%d"%(x,y))
    x,y=exchange(x,y)
    print("x=%d,y=%d"%(x,y))