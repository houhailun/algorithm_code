#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目描述：输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的

输出描述：对应每个测试案例，输出两个数，小的先输出

解题思路：设置两个变量start，end，start从头开始，end从尾部开始，求start+end是否为S
    若等于S,则记录该序列，相差越远乘积越小
    若小于S,则end+1；
    大于S,则start-1
    注意：不需要遍历到S，因为至少要由两个数的和是S
"""


class Solution:
    def find_numbers_with_sum(self, array, tsum):
        if not array or tsum == 0:
            return []

        ret = []
        start, end = 0, len(array)-1
        while start < end:
            cur_sum = array[start] + array[end]
            if cur_sum == tsum:
                ret.append(array[start])
                ret.append(array[end])
                break
            elif cur_sum > tsum:
                end -= 1
            else:
                start += 1

        return ret


if __name__ == "__main__":
    cls = Solution()
    print(cls.find_numbers_with_sum([1,2,4,7,11,15], 15))