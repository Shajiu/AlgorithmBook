# -*- coding: utf-8 -*-
# @Time    : 2020/3/23 17:37
# @Author  : shajiu
# @FileName: test68.py
# @Software: PyCharm
if __name__ == '__main__':
    person={"li":18,"wang":50,"zhang":20,"sun":22}
    m="li"
    for key in person.keys():
        if person[m]<person[key]:
            m=key
    print("%s,%d"%(m,person[m]))