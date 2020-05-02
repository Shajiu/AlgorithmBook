# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 19:38
# @Author  : shajiu
# @FileName: test31.py
# @Software: PyCharm
num=input("请您输入一个五位数字\n")
number=num
if len(num)!=5:
    print("请您一定输入5位数字！！！")
    num = input("请您输入一个五位数字\n")
m=[v for v in num]
if m[0]==m[-1] and m[1]==m[-2]:
    print("数字",number,"为回文数")
else:
    print("数字",number,"不是回文数")
