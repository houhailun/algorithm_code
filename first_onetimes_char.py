#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目要求：在字符串中找到第一次出现一次的字符

思路：诸如这种求出现次数的字符串，由于字符串范围为0~255（char为1字节，0~2**8-1），所以可以用哈希表来快速实现，字符的ascii值作为下表，出现的次数作为哈希表值

本题要求第一个只出现一次的字符，所以还需要根据字符串顺序依次来判断是否只出现一次

时间复杂度：O(n)
"""


class FirstNotRepeatingChar:
    def __init__(self, s):
        self.s = s
        self.hash = [0]*256

    def first_one_time_char(self):
        # 构建哈希表
        for ch in self.s:
            self.hash[ord(ch)] += 1

        # 查找第一个出现一次的字符
        for ch in self.s:
            if self.hash[ord(ch)] == 1:
                return ch
        return None


if __name__ == "__main__":
    cls = FirstNotRepeatingChar("aabbcdcdffess")
    print(cls.first_one_time_char())
