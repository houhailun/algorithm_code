#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：字符流中第一个不重复的字符

题目描述：请实现一个函数用来找出字符流中第一个只出现一次的字符。
    例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

解题思路：当类似找字符的次数等问题，都可以用哈希表来实现；本题是要找第一个只出现一次的字符，只需要最后按照字符流顺序检查即可
"""


class Solution:
    def __init__(self):
        self.table = [0]*256
        self.ret = []

    def first_appearing_once(self):
        if not self.table:
            return '#'

        for ch in self.ret:
            if self.table[ord(ch)] == 1:
                return ch
        return '#'

    def insert(self, char):
        self.table[ord(char)] += 1
        self.ret.append(char)


if __name__ == "__main__":
    cls = Solution()
    cls.insert('g')
    print(cls.first_appearing_once())