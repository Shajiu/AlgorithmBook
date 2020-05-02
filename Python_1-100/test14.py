# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 11:32
# @Author  : shajiu
# @FileName: test14.py
# @Software: PyCharm
import string
s=input("请您输入一个字符串!")
letters=0
space=0
digit=0
others=0
i=0

while i < len(s):
    c=s[i]
    i+=1
    if c.isalpha():    #判断字符
        letters+=1
    elif c.isspace():  #判断空格
        space+=1
    elif c.isdigit():  #判断数字
        digit+=1
    else:
        others+=1      #其他符号
print('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))