# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 17:00
# @Author  : shajiu
# @FileName: test64.py
# @Software: PyCharm
if __name__ == '__main__':
    a=[1,3,2]
    b=[3,4,5]
    a.sort()   #对列表a进行排序
    print(a)

    #连接列表a与b
    print(a+b)

    #连接列表a与b
    a.extend(b)
    print(a)