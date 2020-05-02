# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 20:14
# @Author  : shajiu
# @FileName: test33.py
# @Software: PyCharm
a=["aa","bb","cc","dd","ee"]
for i in range(len(a),0,-1):
    print('测试段:',a[i-1])

for i in a[::-1]:
    print(i)