# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 19:47
# @Author  : shajiu
# @FileName: Count Primes.py
# @Software: PyCharm
def countPrimes(n):
    notPrimes=[]

    count=0
    i=2
    for i in n :
        if notPrimes[i]:
            continue
        count+=1
        j=(i)*i
        for j in n:
            notPrimes[int(j)]=True

            return count
if __name__ == '__main__':
    countPrimes(84)