# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 9:01
# @Author  : shajiu
# @FileName: test53.py
# @Software: PyCharm
if __name__ == '__main__':
    a=0x77
    b=a&3
    print("a&b=%d"%b)
    b&=7
    print("a&b=%d"%b)

if __name__ == '__main__':
    a=0x77
    b=a|3
    print("a|b is %d"%b)
    b|=7
    print("a|b is %d"%b)
