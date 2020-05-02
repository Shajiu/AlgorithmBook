# -*- coding: utf-8 -*-
# @Time    : 2020/3/21 20:45
# @Author  : shajiu
# @FileName: test36.py
# @Software: PyCharm
class bcolors:
    HEADER='\033[95m'
    OKBLUE='\033[94m'
    OKGREEN='\033[92m'
    WARNING='\033[91m'
    FAIL='\33[91m'
    ENDC='\033[0m'
    BOLD='\033[1m'
    UNDERLINE='\033[4m'
print(bcolors.HEADER+"警告的颜色字体？"+bcolors.UNDERLINE)