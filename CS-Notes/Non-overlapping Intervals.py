# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 10:25
# @Author  : shajiu
# @FileName: Non-overlapping Intervals.py
# @Software: PyCharm
"""
不重叠的区间个数
"""
def eraseOverlapIntervals(intervals):
    if len(intervals)==0:
        return 0
    sorted(intervals,compare)
    cnt=1
    end=intervals[0][1]
    i=1
    for i in range(len(intervals)) :
        if intervals[i][0]<end:
            continue
        end=intervals[i][1]
        cnt+=1
    return len(intervals)-cnt

def compare(o1,o2):
    return o1[1]-o2[1]

