# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 12:38
# @Author  : shajiu
# @FileName: Friend Circles.py
# @Software: PyCharm


n=0
A=[[1,1,0],
 [1,1,0],
 [0,0,1]]
def findCircleNum(M):
    n=len(M)
    circleNum=0
    hasVisited=[]
    i=0
    for i in n:
        if not hasVisited[i]:
            dfs(M,i,hasVisited)
            circleNum+=1

        return circleNum

def dfs(M,i,hasVisited):
    hasVisited[i]=True
    k=0
    for k in n:
        if M[i][k]==1 and not hasVisited[k]:
            dfs(M,k,hasVisited)
        print("处理完毕!")

if __name__ == '__main__':
    findCircleNum(A)

