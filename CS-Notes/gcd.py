# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 20:02
# @Author  : shajiu
# @FileName: gcd.py
# @Software: PyCharm

"""最大公约数"""
def gcd(a,b):
    if b==0:
        print(a)
    else:
        gcd(b,a%b)

def lcm(a,b):
    c=lcm(a,b)
    print("最小公倍数:",a*b/c)


if __name__ == '__main__':
    gcd(10, 12)
    lcm(10, 12)