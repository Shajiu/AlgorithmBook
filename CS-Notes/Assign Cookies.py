# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 8:56
# @Author  : shajiu
# @FileName: Assign Cookies.py
# @Software: PyCharm

"""
分配饼干
"""
def findContentChildren(grid,size):
    if grid==0 or size==0:
        return 0

    sorted(grid)   #排序
    sorted(size)   #排序

    gi=0
    si=0

    while(gi<len(grid) and si<len(size)):
        if grid[gi]<=size[si]:
            gi+=1
        si+=1
    return gi

if __name__ == '__main__':
    result=findContentChildren([1,3],[1,2,4])
    print(result)