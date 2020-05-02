# -*- coding: utf-8 -*-
# @Time    : 2020/4/7 10:03
# @Author  : shajiu
# @FileName: Two-dimensional_array.py
# @Software: PyCharm
"""
题目描述
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的
顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样
的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = 0
        col = len(array[0]) - 1
        A=False
        while row < len(array) and col >=0:
            if target == array[row][col]:
                print("在内部")
                A=True
                break
            elif target < array[row][col]:
                col -= 1
            elif target > array[row][col]:
                row += 1
            else:
                A=False

        return A


arry =[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]

target =1
tmp = Solution()

if __name__ == '__main__':
    result=tmp.Find(target, arry)
    print(result)