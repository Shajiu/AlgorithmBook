# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 15:50
# @Author  : shajiu
# @FileName: test23.py
# @Software: PyCharm
""""
猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，
又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，
见只剩下一个桃子了。求第一天共摘了多少
"""
x2=1
for day in range(9,0,-1):
    x1=(x2+1)*2
    x2=x1
    print("日期:",day)
print(x1)