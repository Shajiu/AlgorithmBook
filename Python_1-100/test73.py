# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 9:07
# @Author  : shajiu
# @FileName: test73.py
# @Software: PyCharm
if __name__ == '__main__':
    n=0
    p=input("input a octal number:\n")
    for i in range(len(p)):
        n=n*8+ord(p[i])-ord("0")
    print(n)

