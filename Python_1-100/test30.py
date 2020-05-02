# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 19:05
# @Author  : shajiu
# @FileName: test30.py
# @Software: PyCharm

number=int(input("请输入一个数字\n"))
a=number//10000
b=number//1000%10
c=number//100%10
d=number//10%10
e=number%10
print(e,d,c,b,a)
