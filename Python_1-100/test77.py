# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 10:34
# @Author  : shajiu
# @FileName: test77.py
# @Software: PyCharm
if __name__ == '__main__':
    class student:
        x=0
        c=0
    def f(stu):
        stu.x=20
        stu.c="c"
    a=student()
    a.x="a"
    a.c="a"
    f(a)
    print(a.x,a.c)