# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 8:51
# @Author  : shajiu
# @FileName: test06.py
# @Software: PyCharm
def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
        return a

#输出了第10个斐波那契数列
print(fib(10))

def fib_2(n):
    if n==1 or n==2:
        return 1
    return fib_2(n-1)+fib_2(n-2)

#输出了第10个斐波那契数列
print(fib_2(10))



def fib(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fibs=[1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
#输出前10个斐波那契数列
print(fib(10))
