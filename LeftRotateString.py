#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目描述：左旋转字符串 对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”

解题思路：方法一：可以简单把前k位当作str1，后N位当作str2，直接str2+str1；缺点：针对n大于s长度时不生效
        方法二：利用s翻转len(s)后仍然是s，则最终移位n%len(s)
        方法二：利用三次翻转
"""


class Solution:
    def left_rotate_string(self, s, n):
        # 当n大于s的长度时出现问题，不进行翻转
        if not s or n <= 0:
            return s
        str1 = s[:n]
        str2 = s[n:]
        return str2+str1

    def left_rotate_string_2(self, s, n):
        if not s or n <= 0:
            return

        n = n % len(s)  # 解决n大于s长度的问题
        return s[n:]+s[:n]

    def left_rotate_string_3(self, s, n):
        if not s or n <= 0:
            return s

        n = n % len(s)  # 解决n大于len（s）的问题

        # 字符串是不可变对象，不能通过下表改变值，这里转换为list
        s = list(s)
        self.reverse(s, 0, n-1)         # 翻转前字串
        self.reverse(s, n, len(s)-1)    # 翻转后字串
        self.reverse(s, 0, len(s)-1)  # 翻转整个字符串
        return ''.join(s)  # 转换位str

    def reverse(self, s, start, end):
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


if __name__ == "__main__":
    cls = Solution()
    print(cls.left_rotate_string('abcdfge', 8))
    print(cls.left_rotate_string_2('abcdfge', 8))
    print(cls.left_rotate_string_3('abcdfge', 8))