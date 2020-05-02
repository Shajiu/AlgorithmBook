# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 10:07
# @Author  : shajiu
# @FileName: test55.py
# @Software: PyCharm
if __name__ == '__main__':
    a=int(input("input a number\n"))
    b=a>>4
    c=~(~0<<4)
    d=b&c
    print("%o\t%o"%(a,d))