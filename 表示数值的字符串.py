#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：表示数值的字符串

题目描述：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。 但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是

解题思路：本题考察什么是数值，异常情况的全面考虑
    1、数值：由数字组成，第一位可以是符号，可以是e表示
    2、异常情况：（1）存在非数字字母（2）符号只能出现在第一位或者e后面的第一位（3）e后面不能有小数 (4)e只能出现一次，e不能再最后一位
"""


class Solution:
    def is_numeric(self, s):
        if not s:
            return False

        sign = has_e = dec = False
        for i in range(len(s)):
            if s[i] == 'E' or s[i] == 'e':
                if has_e or i == len(s)-1:  # e只能出现一次且后面必须跟数字(e不能是最后一位)
                    return False
                has_e = True
            elif s[i] == '+' or s[i] == '-':
                if sign and s[i-1] != 'e' and s[i-1] != 'E':  # 正负号只能出现在最头或者E后面
                    return False
                sign = True
            elif s[i] == '.':  # 小数点只能出现一次，且不能出现在e后面
                if has_e or dec:
                    return False
                dec = True
            elif s[i] < '0' or s[i] > '9':
                return False

        return True

    def is_numeric_2(self, s):
        # 利用内置函数float实现
        try:
            float(s)
            return True
        except:
            return False


if __name__ == "__main__":
    cls = Solution()
    print(cls.is_numeric('123e3.4'))