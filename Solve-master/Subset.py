# -*- coding: utf-8 -*-
# @Time    : 2020/3/30 15:41
# @Author  : shajiu
# @FileName: Subset.py
# @Software: PyCharm
"""
input:   ['a', 'b', 'c', 'd', 'e', 'f']
output: list，包含所有字符的组合
"""
list_demo = ['a', 'b', 'c', 'd', 'e', 'f']
sub_list_all = []
#  1 << len(list_demo)表示
for i in range(1 << len(list_demo)):
    combo_list = []
    for j in range(len(list_demo)):
        if i & (1 << j):
            combo_list.append(list_demo[j])
    sub_list_all.append(combo_list)
print(sub_list_all)
print(len(sub_list_all))
