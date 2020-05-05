# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 16:20
# @Author  : shajiu
# @FileName: Two Sum.py
# @Software: PyCharm
#   有序数组的 Two Sum
def tow_sum(numbers,target):
    if numbers==0:
        return 0
    i=0
    j=len(numbers)-1
    while i<j:
        sum=0
        sum=numbers[i]+numbers[j]
        if sum==target:
            print(i,j)
            return numbers[i],numbers[j]
        elif sum<target:
            i+=1
        else:
            j-=1
    return 0

if __name__ == '__main__':
    num=[2, 7, 11, 15]
    target = 9
    tow_sum(num,target)

