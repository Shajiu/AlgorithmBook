# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 19:03
# @Author  : shajiu
# @FileName: test42.py
# @Software: PyCharm
if __name__ == '__main__':
    a=[9,6,5,4,1]
    N=len(a)
    print(a)
    c=[]
    for i in range(N):
        c.append(a[N-i-1])
    print(c)

