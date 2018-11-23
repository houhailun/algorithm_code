#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：翻转单词顺序列

题目描述：例如，“student. a am I”，把句子单词的顺序翻转了，正确的句子应该是“I am a student.”

解题思路：利用字符串翻转，第一次翻转整个句子，第二次翻转每个单词；单词是以空格为结束标记

基础知识：str.split() --把字符串切分为列表    ’‘.join -- 列表拼接为字符串
"""


class Solution:
    def reverse_sentence(self, s):
        if not s:
            return s

        # 第一次翻转整个句子
        ret = []
        s = self.reverse(list(s), 0, len(s)-1)

        # 第二次翻转每个单词
        word_list = s.split(' ')  # 切分为单词列表
        for word in word_list:
            ret.append(self.reverse(list(word), 0, len(word)-1))

        return ' '.join(ret)

    def reverse(self, s, start, end):
        while start <= end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(s)


if __name__ == "__main__":
    cls = Solution()
    print(cls.reverse_sentence('student. a am i'))