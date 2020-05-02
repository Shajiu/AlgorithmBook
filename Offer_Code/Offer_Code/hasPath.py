# -*- coding: utf-8 -*-
# @Time    : 2020/5/1 19:20
# @Author  : Shajiu
# @FileName: hasPath.py
# @Software: PyCharm
# @Github  ：https://github.com/Shajiu
'''
题目；
   请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
   路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，
   向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
    例如 \begin{bmatrix} a & b & c &e \\ s & f & c & s \\ a & d & e& e\\
     \end{bmatrix}\quad    矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"
     abcb"路径，因为字符串的第一 个字符b占据了矩阵中的第一行第二个格子之后，
     路径不能再次进入该格子。
'''


class Solution:
    def is_path(self, matrix, x, rows, y, cols, path, index, length, mark):
        """当前这格填写是否正确，如果填写正确，再去看他的

        :param matrix:
        :param rows:
        :param cols:
        :param path:
        :param length:
        :return:
        """
        if index == length:
            return True
        # 本次位置为一个非法的位置或者已经访问过或者填写不匹配
        # 直接返回False
        # 没填写完毕已经越界
        if x >= rows or x < 0 or y >= cols or y < 0:
            return False
        # 当前位置已经被访问过
        if mark[x][y]:
            return False
        # 当前位置填写的数字不对
        if path[index] != matrix[x * cols + y]:
            return False
        # 否则说明这个位置是合法的位置，可以进行填写
        # 并且可以进行下一步扩展
        # 返回下一步填写的情况
        mark[x][y] = True  # 标记为已经访问
        index += 1  # 开始进入下一个位置
        # 去周围的4个方向搜索，找到一个方向满足要求，即可往下进行
        up = self.is_path(matrix, x - 1, rows, y, cols, path, index, length, mark)
        down = self.is_path(matrix, x + 1, rows, y, cols, path, index, length, mark)
        left = self.is_path(matrix, x, rows, y - 1, cols, path, index, length, mark)
        right = self.is_path(matrix, x, rows, y + 1, cols, path, index, length, mark)
        result = up or down or left or right
        # 失败的本次填写
        # 4个方向都不对，因此说明x,y的这个位置不能这样匹配
        if not result:
            # 一定要把填错的数字改回来，回朔法
            mark[x][y] = False
            index -= 1  # 还进入这个位置的匹配
        # 如果最终填写正确，意味着每步都可以进入if语句，最终抵达开头的index=length的语句
        # 每次一定在4个中有一个可以往下扩展，进入这个if语句，最终抵达true,层层返回，而且没有必要去清除标记
        # 否则就说明4个路径都不对，无法搞，中途就夭折了，确实这一步就失败了，层层返回False
        return result

    def hasPath(self, matrix, rows, cols, path):
        """最开始的递归程序：由于不知道开始选取那个字母作为第一个递归程序的入口
        所以需要遍历整个迷宫

        :param matrix:
        :param rows:
        :param cols:
        :param path:
        :return:
        """
        if not matrix or rows <= 0 or cols <= 0 or not path:
            return False
        # 设置访问标记位
        mark = [[False for i in range(cols)] for j in range(rows)]
        # 遍历整个迷宫，寻找入口
        for i in range(rows):
            for j in range(cols):
                result = self.is_path(matrix, i, rows, j, cols, path, 0, len(path), mark)
                if result:
                    return True  # 寻找到正确的路径
        return False