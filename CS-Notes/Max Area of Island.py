# -*- coding: utf-8 -*-
# @Time    : 2020/3/7 17:41
# @Author  : shajiu
# @FileName: Max Area of Island.py
# @Software: PyCharm
import math

direction=[{0,1},{0,-1},{1,0},{-1,0}]
m=0
n=0
def maxAreaOfIsland(grid):
    if grid==0 or len(grid)==0:
        return 0
    m=len(grid)
    n=len(grid[0])
    maxArea=0
    i=0
    for i in range(m):
        j=0
        for j in range(n):
            maxArea=max(maxArea,dfs(grid,i,j))
        return maxArea

def dfs(grid,r,c):
    if r<0 or r>=m or c<0 or c>=n or grid[r][c]==0:
        return 0
    grid[r][c]=0
    area=1
    for d in direction:
        area+=dfs(grid,r+d[0],c+d[1])
    return area
h=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

if __name__ == '__main__':
    a=maxAreaOfIsland(h)
    print(a)

