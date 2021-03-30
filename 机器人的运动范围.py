#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：机器人的运动范围

题目描述：地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。
    例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
    但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

解题思路：上一题的基础上添加了限制条件：不能进入行坐标和列坐标的数位之和大于k的格子
    在能进入的格子中设置为1，最后统计1的个数
"""


class Solution:
    def moving_count(self, threshold, rows, cols):
        """
        机器人的运动范围
        :param threshold: 限制阈值
        :param rows: 行数
        :param cols: 列数
        :return:
        """
        if threshold <= 0 or rows <= 0 or cols <= 0:
            return 0
        # 设置行数为rows，列数为cols的列表
        mat = [0] * rows * cols
        self.moving_helper(mat, threshold, rows, cols, 0, 0)
        return mat.count(1)

    def moving_helper(self, mat, threshold, rows, cols, i, j):
        # 判断条件：i，j都在有效范围，且当前格子符合限制条件，且没有走过这个格子（避免重复）
        if 0 <= i < rows and 0 <= j < cols and self.limit_conf(threshold, i, j) and mat[i*cols+j] == 0:
            mat[i*cols+j] = 1
            self.moving_helper(mat, threshold, rows, cols, i+1, j)
            self.moving_helper(mat, threshold, rows, cols, i-1, j)
            self.moving_helper(mat, threshold, rows, cols, i, j-1)
            self.moving_helper(mat, threshold, rows, cols, i, j+1)

    def limit_conf(self, threshold, i, j):
        """
        限制条件函数，使用map实现可有效减小代码量
        抽象为函数好处L:可以灵活设置限制条件
        """
        if sum(map(int, str(i)+str(j))) <= threshold:
            return True
        return False


if __name__ == "__main__":
    cls = Solution()
    print(cls.moving_count(9, 12, 12))