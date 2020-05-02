# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 10:15
# @Author  : shajiu
# @FileName: test10.py
# @Software: PyCharm
import time
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
#暂停一秒
time.sleep(1)
print (time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))