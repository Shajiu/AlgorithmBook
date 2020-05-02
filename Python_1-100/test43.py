# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 19:31
# @Author  : shajiu
# @FileName: test43.py
# @Software: PyCharm
def varfunc():
    var=0
    print("var=%d"%var)
    var+=1
if __name__ == '__main__':
    for i in range(3):
        varfunc()


#类的属性
#作为类的一个属性吧
class Static:
    StaticVar=5
    def varfunc(self):
        self.StaticVar+=1
        print(self.StaticVar)

print(Static.StaticVar)
a=Static()
for i in range(3):
    a.varfunc()


class func:
    fu=10
    def ff(self,fu):
        fu+=1
        print(fu)

c=func()
print("测试段1:",c.fu)
print("测试段2:",c.ff(10))