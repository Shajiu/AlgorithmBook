# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 9:34
# @Author  : shajiu
# @FileName: test75.py
# @Software: PyCharm
sum=4
s=4
for j in range(2,9):
    print(sum)
    if j<=2:
        s*=7
    else:
        s*=8
    sum+=s
print("sum=%d"%sum)