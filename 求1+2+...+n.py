#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目:求1+2+...+n

题目描述：求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）

解题思路：可以利用类的构建函数来实现
"""


class Solution:
    def get_sum_1(self, n):
        """利用python的语言特性"""
        if n <= 0:
            return -1

        return sum(list(range(n+1)))

    def get_sum_2(self, n):
        """递归"""
        ans = n
        if ans > 0:
            ans += self.get_sum_2(n-1)
        return ans


if __name__ == "__main__":
    cls = Solution()
    print(cls.get_sum_1(5))
    print(cls.get_sum_2(1))