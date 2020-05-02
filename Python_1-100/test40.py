# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 12:09
# @Author  : shajiu
# @FileName: test40.py
# @Software: PyCharm
if __name__ == '__main__':
    a=[]
    sum=0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input("input num:\n")))
    for i in range(3):
        sum+=a[i][i]
    print(sum)


a=[]
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(float(input("请您输入对应的数字")))
    sum+=a[i][i]
print(sum)
