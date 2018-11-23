#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目描述：输出所有和为S的连续正数序列，序列内安装从小到大的顺序，序列间按照开始数字从小到大的顺序

解题思路：设置两个变量start，end，从1开始，end逐个累加，求start到end的和是否为S
    若等于S,则记录该序列，start+1，end+1
    若小于S,则end+1；
    大于S,则start+1
    注意：不需要遍历到S，因为至少要由两个数的和是S，因此start<=S//2
"""


class Solution:
    def find_continuous_sequence(self, tsum):
        if tsum <= 0:
            return None

        start, end = 1, 2
        ret = []
        while start != (1+tsum)//2:
            cur_sum = self.sequence_add(start, end)
            if tsum == cur_sum:
                tmp = []
                for i in range(start, end+1):
                    tmp.append(i)
                ret.append(tmp)
                start += 1
            elif tsum > cur_sum:
                end += 1
            else:
                start += 1
        return ret

    def sequence_add(self, start, end):
        ret = 0
        for i in range(start, end+1):
            ret += i
        return ret


if __name__ == "__main__":
    cls = Solution()
    print(cls.find_continuous_sequence(15))


