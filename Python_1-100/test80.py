# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 16:07
# @Author  : shajiu
# @FileName: test80.py
# @Software: PyCharm
if __name__ == '__main__':
    import time
    print(time.ctime(time.time()))
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))

if __name__ == '__main__':
    import time
    start=time.time()
    for i in range(300):
        print(i)
    end=time.time()

    print(end-start)


if __name__ == '__main__':
    import time
    start=time.clock()
    for i in range(1000):
        print(i)
    end=time.clock()
    print("different is %6.3f"%(end-start))

from dateutil import parser
dt=parser.parse("Aug 28 2015 12:00AM")
print(dt)