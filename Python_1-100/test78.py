# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 10:57
# @Author  : shajiu
# @FileName: test78.py
# @Software: PyCharm
if __name__ == '__main__':
    n=1
    while n<=7:
        a=int(input("input a number:\n"))
        while a<1 or a>50:
            a=int(input("input a number:\n"))
        print(a*"*")
        n+=1