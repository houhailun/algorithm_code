#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：扑克牌顺子

题目描述：判断排是否是顺子，A-1，J-11，Q-12，K-13，大小王可以当作任意牌，为方便统计，可以认为是0

解题思路：
    方法一：先排序，检查0的个数，检查间隔的牌数，如果间隔的牌数大于0的个数，则不是顺子
    方法二：用hash表来做，避免了排序，只需计算最大的键值和最小的键值的差，若小于4，不需考虑有多少大小王，都可以组成顺子。
"""


class Solution:
    def is_continuous(self, numbers):
        if not numbers or len(numbers) < 5:
            return False
        numbers.sort()

        num_of_zero = numbers.count(0)  # 大小王的个数
        num_of_gap = 0
        for ix in range(num_of_zero+1, len(numbers)):
            if numbers[ix] == numbers[ix-1]:
                return False
            num_of_gap += numbers[ix]-numbers[ix-1]-1

        print("num_of_gap:%d, num_of_zero:%d" % (num_of_gap, num_of_zero))
        return False if num_of_gap > num_of_zero else True

    def is_continuous_2(self, numbers):
        if not numbers or len(numbers) < 5:
            return False

        cards = {}
        for num in numbers:
            if num == 0:
                continue
            if num in cards.keys():  # 重复牌
                return False
            else:
                cards[num] = 1
        return True if max(cards.keys())-min(cards.keys()) < 4 else False


if __name__ == "__main__":
    cls = Solution()
    print(cls.is_continuous([0,1,2,3,6]))
    print(cls.is_continuous_2([0,1,2,3,6]))