# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 8:56
# @Author  : shajiu
# @FileName: test17.py
# @Software: PyCharm
tour=[]
height=[]
hei=100.0
tim=10
for i in range(1,tim+1):
    if i ==1:
        tour.append(hei)
    else:
        tour.append(2*hei)
    hei/=2
    height.append(hei)

print("总高度:tour={0}".format(sum(tour)))
print("第10次反弹高度:height={0}".format(height[-1]))