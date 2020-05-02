# -*- coding: utf-8 -*-
# @Time    : 2020/3/22 9:43
# @Author  : shajiu
# @FileName: test38.py
# @Software: PyCharm


num=[12,23,14,27,45,67,78,89,45,20]
def insert_sort(arr):
    for i in range(len(arr)-1):
        if arr[i+1]<arr[i]:  #如果arr[i+1]较小、将其插入到前面升序序列中
            for j in range(i+1,0,-1):
                if arr[j]<arr[j-1]: #依次将大于arr[i+1]的值向后移动，直到找到不大于arr[i+1]的值
                   arr[j-1],arr[j]=arr[j],arr[j-1]#依次将大于arr[i+1]的值向后移动，直到找到不大于arr[i+1]的值
                else:
                    break
            print(arr)
            return arr
if __name__ == '__main__':
    insert_sort(num)
