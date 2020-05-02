# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 19:45
# @Author  : shajiu
# @FileName: test32.py
# @Software: PyCharm
week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
we=input("请您输入星期\n")
def wee_(we):
    for w in we:
        for v in week:
            if w in v:
                print("为星期:", v)
                break
            else:
                print("输入有误!!!\n请您将首字母大写!!!")
                we = input("请您输入星期\n")
                wee_(we)
                break

if __name__ == '__main__':
    wee_(we)
