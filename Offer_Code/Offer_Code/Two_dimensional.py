# -*- coding: utf-8 -*-
# @Time    : 2020/4/21 14:21
# @Author  : Shajiu
# @FileName: Two_dimensional.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
class Solution:
    """matrix类型为二维列表，需要返回列表"""
    def printMatrix(self,matrix):
        """write code here"""
        result=[]
        while matrix:
            result=result+matrix.pop(0)
            if not matrix:
                break
            matrix=self.turn(matrix)
        return result
    def turn(self,matrix):
        r=len(matrix)
        c=len(matrix[0])
        B=[]
        for i in range(c):
            A=[]
            for j in range(r):
                A.append(matrix[j][i])
            B.append(A)
        B.reverse()
        return B

AB=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
if __name__ == '__main__':
    result=Solution()
    print(result.printMatrix(AB))