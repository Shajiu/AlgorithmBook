# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 12:25
# @Author  : shajiu
# @FileName: Best Time to Buy and Sell Stock.py
# @Software: PyCharm
def maxProfit(prices):
    profit=0
    i=1
    while i<len(prices):
        if prices[i]>prices[i-1]:
            profit+=(prices[i]-prices[i-1])
        i+=1

    return profit

if __name__ == '__main__':
    resut=maxProfit([1,3,4,5,2])
    print(resut)