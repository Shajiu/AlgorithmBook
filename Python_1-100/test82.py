# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 16:29
# @Author  : shajiu
# @FileName: test82.py
# @Software: PyCharm
if __name__ == '__main__':
    fp=open("test.txt","w")
    string=input("please input a string：")
    string=string.upper()
    fp.write(string)
    fp=open("test.txt","r")
    print(fp.read())
    fp.close()