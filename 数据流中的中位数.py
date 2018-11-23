#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：数据流中的中位数

题目描述：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
    我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

解题思路：
    方法1：先把数据流数据全部存储起来，然后排序求中位数，同时注意检查是偶数还是奇数
    方法2：利用heapq模块实现,heappush()自动调整为最小堆
"""
import heapq
import math

class Solution:
    def __init__(self):
        self.data = []
        self.cnt = 0

    def Insert(self, num):
        self.data.append(num)
        self.cnt += 1

    def GetMedian(self):
        self.data.sort()
        if self.cnt % 2 == 1:
            return self.data[self.cnt // 2]
        else:
            return (self.data[(self.cnt+1) // 2] + self.data[(self.cnt-1) // 2]) / 2

    def insert(self, num):
        heapq.heappush(self.data, num)

    def get_modian(self):
        mid = math.ceil(len(self.data) / 2)      # 向上取整
        q = heapq.nlargest(mid, self.data)[-1]   # 最大的mid个数中的最小值
        p = heapq.nsmallest(mid, self.data)[-1]  # 最小的mid个数中的最大值

        return (p+q) / 2


if __name__ == "__main__":
    cls = Solution()
    a = [3,4,2,7,8,4,7,5,8,3]
    for i in a:
        cls.insert(i)
    print(cls.data)
    print(cls.get_modian())