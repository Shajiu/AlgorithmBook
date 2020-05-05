# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 12:30
# @Author  : shajiu
# @FileName: socket.py
# @Software: PyCharm
import socket
s=socket.socket()      #创建socket对象
host=socket.socket()   #获取本地主机名称
port=12345             #设置端口
s.bind((host,port))    #绑定端口

s.bind(5)
while True:
    c,addr=s.accept()  #建立客户断链接
    print("链接地址:",addr)
    c.send("欢迎访问菜鸟教程！！！")
    c.close()  #关闭链接