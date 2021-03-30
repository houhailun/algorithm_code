#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：把字符串转换为整数

题目描述：要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。

解题思路：
    方法1：利用python的内置函数int()实现
    方法2：主要是考察是否能考虑到输入是不合法的字符串，包括：有非数字字符串、空格、空字符等情况；最开始处的+/-号是合法的
        数字字符串转换为整数核心公式：num = num*10 + ord(s)-ord('0')；ord()返回字符串的ASCII码
"""


class Solution:
    def str_to_int(self, s):
        # 非法字符串返回0
        if not s:
            return 0

        # 开头的正负号合法
        positive = True
        if s[0] == '-':
            positive = False

        # 出现非数字字符
        for i in range(1, len(s)):
            if not s[i].isdigit():
                return 0

        ret = self.to_str(s)
        return ret if positive else (0-ret)

    def to_str(self, s):
        ret = s
        if s[0] == '+' or s[0] == '-':
            ret = s[1:]

        num = 0
        for st in ret:
            num = num*10 + ord(st) - ord('0')
        return num


if __name__ == "__main__":
    cls = Solution()
    print(cls.str_to_int('1243'))
