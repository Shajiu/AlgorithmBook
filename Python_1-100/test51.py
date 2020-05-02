# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 8:51
# @Author  : shajiu
# @FileName: test51.py
# @Software: PyCharm
MAXIMUM=lambda x,y:(x>y)*x+(x<y)*y
MINIMUM=lambda x,y:(x>y)*y+(x<y)*x

if __name__ == '__main__':
    a=10
    b=20
    print("The largar one is %d"%MAXIMUM(a,b))
    print("The largar one is %d"%MINIMUM(a,b))