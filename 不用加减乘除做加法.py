#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目名称:不用加减乘除做加法

题目描述:写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号

解题思路:可以利用位与操作
    step1:不考虑进位，num1^num2(相同为0，不同为1，和num1+num2时相同的)
    step2：考虑进位，只有num1和num2的某位全是1时才会进位，也就是num1&num2
    step3：当num1&num2 != 0 表示有进位，此时把(num1&num2)<<1和num1^num2重新做step1和step2操作，直到num1&num2=0

NOTE:(n1&n2)<<1这一步int overflow的时候，python会自动转成long,其他语言会溢出
"""


class Solution:
    def add(self, num1, num2):
        while num2 != 0:
            sum = (num1 ^ num2)
            carray = ((num1 & num2) << 1) & 0xFFFFFFFF
            if carray > 0x7FFFFFFF:  #  carry
                carray = -((~carray-1) & 0xFFFFFFFF)
            num1 = sum
            num2 = carray
        return num1


if __name__ == "__main__":
    cls = Solution()
    print(cls.add(-7, 2))