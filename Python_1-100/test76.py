# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 9:42
# @Author  : shajiu
# @FileName: test76.py
# @Software: PyCharm
delimiter=' '
mylist=["Brazil","Russia","India","China"]
print(delimiter.join(mylist))

a=9
i=1
j=int(input("输入一个数字:\n"))
while a%j!=0:
    a=str(a)*i
    a=int(a)
    i+=1
print("输入为:",j)
print("被除数为:",a)


if __name__ == '__main__':
    a="acegikm"
    b="bdfhjlnpd"
    #链接字符串


