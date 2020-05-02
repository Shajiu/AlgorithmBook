# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 11:05
# @Author  : shajiu
# @FileName: test13.py
# @Software: PyCharm
def reduceNum(n):
    print("{}=".format(n))
    if not isinstance(n,int) or n <=0:
        print("请输入一个正确的数字!")
        exit(0)
    elif n in [1]:
        print("{}".format(n))
    while n not in [1]:#循环保证递归
        for index in range(2,n+1):
            if n %index==0:
                n/=index # n等于n/index
                if n ==1:
                    print(index)
                else:#index一定是素数
                    print("{}*".format(index))
                break

reduceNum(90)
reduceNum(100)