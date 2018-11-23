#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
题目：滑动窗口的最大值

题目描述：给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
    他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}，
    {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}

解题思路：异常情况：数组为空，滑动窗口大于数组长度；假设数组长度为n，滑动窗口长度为k（n>=k），则可以有n-k+1种滑动可能
    方法：每次针对滑动窗口内的数字使用max求最大值
"""


class Solution:
    def max_in_windows(self, num, size):
        """
        滑动窗口最大值实现函数
        :param num: 数组
        :param size: 滑动窗口大小
        :return: [] or 滑动窗口的最大值
        """
        # 异常情况
        if not num or size > len(num) or size <= 0:
            return []

        res = []
        for i in range(len(num)-size+1):
            windows_first, window_last = i, size-1+i*1  # 滑动窗口的起始坐标、结束坐标
            window = num[windows_first:window_last+1]   # 滑动窗口的数据
            res.append(max(window))

        return res


if __name__ == "__main__":
    cls = Solution()
    print(cls.max_in_windows([2, 3, 4, 2, 6, 2, 5, 1], 3))
