# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 8:28
# @Author  : shajiu
# @FileName: built-in function.py
# @Software: PyCharm
""""各种内置函数"""
#求绝对值的计算
print(abs(-10))

#商和余数一起计算
print(divmod(7,3))


#从控制台输入
# a=input("input")
# print("您输入的为:",a)

import re
print(re.match("www","www.runoob.com").span())  #在起始位置匹配
print(re.match("com","www.runoob.com"))         #不在起始位置匹配

line="Cats are smarter than dogs"
matchObj=re.match(r"(.*)are(.*?).",line,re.M|re.I)
if matchObj:
    print("matchObj.group():",matchObj.group())
    print("matchObj.group(1):",matchObj.group(1))
    print("matchObj.group(2):",matchObj.group(2))
else:
    print("No match!!")