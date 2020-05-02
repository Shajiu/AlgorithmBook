# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 16:55
# @Author  : shajiu
# @FileName: test63.py
# @Software: PyCharm
if __name__ == '__main__':
    ptr=[]
    for i in range(5):
        num=int(input("please input a number"))
        ptr.append(num)
    print(ptr)
    ptr.reverse()
    print(ptr)