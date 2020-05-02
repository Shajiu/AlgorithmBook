# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 20:28
# @Author  : shajiu
# @FileName: test35.py
# @Software: PyCharm
def hello_world():
    print("hello world")
def three_hellos():
    for i in range(3):
        hello_world()
if __name__ == '__main__':
    three_hellos()