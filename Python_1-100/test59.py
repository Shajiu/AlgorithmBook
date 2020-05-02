# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 15:50
# @Author  : shajiu
# @FileName: test59.py
# @Software: PyCharm
n1=int(input("请输入第一个数字"))
n2=int(input("请输入第二个数字"))
n3=int(input("请输入第三个数字"))
def wsp(p1,p2):
    return p2,p1
if n1>n2:
    n1,n2=wsp(n1,n2)
if n1>n3:
    n1,n3=wsp(n1,n3)
if n2>n3:
    n2,n3=wsp(n2,n3)
print(n1,n2,n3)
