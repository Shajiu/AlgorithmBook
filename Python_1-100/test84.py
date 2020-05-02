# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 16:33
# @Author  : shajiu
# @FileName: test84.py
# @Software: PyCharm
if __name__ == '__main__':
    import string
    fp=open("test.txt")
    a=fp.read()
    fp.close()

    fp=open("test2.txt")
    b=fp.read()
    fp.close()

    fp=open("test3.txt","w")
    l=list(a+b)
    l.sort()
    s=''
    s=s.join(l)
    fp.write(s)
    fp.close()
