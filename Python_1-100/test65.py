# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 17:05
# @Author  : shajiu
# @FileName: test65.py
# @Software: PyCharm
if __name__ == '__main__':
    for i in range(5):
        n=0
        if i!=1:n+=1
        if i==3:n+=1
        if i==4:n+=1
        if i!=4:n+=1
        if n==3:print(64+1)