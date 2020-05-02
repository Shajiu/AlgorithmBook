# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 9:54
# @Author  : shajiu
# @FileName: test09.py
# @Software: PyCharm
import time

myD={1:"a",2:"b"}
for key,value in dict.items(myD):
    print(key,value)
    time.sleep(1) #暂停1秒
