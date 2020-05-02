# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 18:22
# @Author  : shajiu
# @FileName: test21.py
# @Software: PyCharm
from sys import stdout
for i in range(4):
    for j in range(2-i+1):
        stdout.write(" ")
    for k in range(2*i+1):
        stdout.write("*")
    print()

for i in range(3):
    for j in range(i+1):
        stdout.write(" ")
    for k in range(4-2*i+1):
        stdout.write("*")
    print()

