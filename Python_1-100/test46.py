# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 21:57
# @Author  : shajiu
# @FileName: test46.py
# @Software: PyCharm
x=[[12,22,34],
   [12,34,56],
   [33,22,43]]

y=[[23,58,69,],
   [54,85,78],
   [98,78,24]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(x)):
    #迭代输出列
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
for i in result:
    print(i)