#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目说明：一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。

解题思路：对于出现两次的数可以根据二进制异或（相同为0，不同为1;0与任何值异或后都不改变任意值）
    1、全部数字异或，结果得到的其实就是只出现一次的数字的异或结果
    2、由于这两个数字异或后必然不为0，则可以根据最低位为1来区分这两个数字
    3、根据最低位是1把数组分为两个数组，每个数组中只有一个数字出现一次，其余数组都出现两次
    4、对两个数组分别异或即可得到只出现一次的数字
"""


class Solution:
    def find_number_appear_once(self, array):
        if array is None or len(array) < 2:
            return None

        # 第一次异或全部数字
        result = 0
        for i in range(len(array)):
            result ^= array[i]

        # 查找result二进制位1的最低位,最低为默认位0
        ix = 0
        while 0x1 & result == 0:
            result = result >> 1
            ix += 1

        # 根据第ix位是否为1，分为两个数组
        arr1 = []
        arr2 = []
        for num in array:
            if num & (0x1 << ix):
                arr1.append(num)
            else:
                arr2.append(num)

        # 两个数组分别异或
        ret1 = ret2 = 0
        for i in range(len(arr1)):
            ret1 ^= arr1[i]
        for i in range( len(arr2)):
            ret2 ^= arr2[i]

        return ret1, ret2


if __name__ == '__main__':
    cls = Solution()
    print(cls.find_number_appear_once([1,1,2,3,4,4,5,6,6,5]))
