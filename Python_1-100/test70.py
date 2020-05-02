# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 17:43
# @Author  : shajiu
# @FileName: test70.py
# @Software: PyCharm
if __name__ == '__main__':
    str1=input("input string:\n")
    str2=input("input string:\n")
    str3=input("input string:\n")

    print(str1,str2,str3)

    if str1>str2:
        str1,str2=str2,str1
    if str1>str3:
        str1,str3=str3,str1
    if str2>str3:
        str2,str3=str3,str2

    print("after being sorted")
    print(str1,str2,str3)