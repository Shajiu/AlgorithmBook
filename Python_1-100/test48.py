# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 8:28
# @Author  : shajiu
# @FileName: test48.py
# @Software: PyCharm
TRUE=1
FALSE=0
def SQ(x):
    return x*x

print("如果输入的数字平方小于50，程序跳出停止运行")

again=1
while again:
    num=int(input("请输入一个数字!"))
    print("运算结果为:%d"%(SQ(num)))
    if SQ(num)>=50:
        again=TRUE
    else:
        again=FALSE
