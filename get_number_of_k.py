#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目要求：统计一个数字在排序数字中出现的次数

解题思路：注意到数组是排序数组，在排序数组中查找一个值是很容易想到二分法的

本题解法：本题暗示关键字可能出现多次，那么如果来查找具体出现多少次呢？利用二分法，查找key，比较左边的值是否等于key，若等于则在左子数组中
         递归查找，找到最左边的位置；同样找到最右边的位置，这样就可以求出总的次数
"""


class Solution:
    def GetNumberOfK(self, data, k):
        if not data:
            return 0

        firstK = self.GetFirstK(data, 0, len(data)-1, k)
        lastK = self.GetLastK(data, 0, len(data)-1, k)
        print('firstK:%d, lastK:%d' % (firstK, lastK))
        if firstK == -1 or lastK == -1:
            return 0

        return lastK-firstK+1

    def GetFirstK(self, data, start, end, k):
        while start <= end:
            mid = (start+end) // 2
            if data[mid] == k:
                if mid == start or data[mid-1] != k:  # 已经是最start 或者 左边的数不等于k，表示已经找到firstK
                    return mid
                end = mid - 1
            elif data[mid] > k:  # 在左子数组中查找
                end = mid - 1
            else:                # 在右子数组中查找
                start = mid + 1
        return -1

    def GetLastK(self, data, start, end, k):
        while start <= end:
            mid = (start + end) // 2
            if data[mid] == k:
                if mid == end or data[mid+1] != k:
                    return mid
                start = mid + 1
            elif data[mid] > k:
                end = mid - 1
            else:
                start = mid + 1
        return -1


if __name__ == "__main__":
    cls = Solution()
    print(cls.GetNumberOfK([1,2,3,3,5,6], 3))