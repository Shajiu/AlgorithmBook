# -*- coding: utf-8 -*-
# @Time    : 2020/4/25 16:46
# @Author  : Shajiu
# @FileName: FindGreatestSumOfSubArray.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
"""
题目:
    HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:
    在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
    但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
    例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
    给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
"""
class Solution:
    """定义两个变量
       一个用来存放之前的累加值、一个用来存储当前的最大和
    """
    def FindGreatestSumOfSubArray(self, array):
        max_sum=int(array[0])  #定义为第一个最大值
        pre_sum=0
        for i in range(len(array)):  #遍历数组中的元素
            if pre_sum<0:
                #如果之前的累加和是小于0的则应该从当前值进行累加
                pre_sum=int(array[i])
            else:
                pre_sum+=int(array[i])
            #如果是大于等于0的则需要将当前的数加到当前
            if pre_sum>max_sum:
                max_sum=pre_sum
        return max_sum
if __name__ == '__main__':
    result=Solution()
    print(result.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2,20]))
