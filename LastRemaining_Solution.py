#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：圆圈中最后剩下的数

题目描述：首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....
    直到剩下最后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

解题思路：约瑟夫环问题，用list来模拟循环列表，当转到第m个小朋友时，pop，并设置标记为-1，下一个为0
"""


class Solution:
    def last_remain_solution(self, n, m):
        if n == 1 or m == 0:
            return -1
        s = [x for x in range(n)]  # 产生等差数列
        p = m - 1
        while len(s) != 1:
            # 这里用while而不是if  因为处理一次后的p可能仍>len(s)-1. 所以必须处理到p值满足list的index条件为止
            while p > len(s) - 1:  # 超过了尾数的index
                # 这个条件要放在最前面,为了防止p一上来就设置的大于len(s)-1
                p = p - (len(s) - 1) - 1  # -1 减1 是因为index从0计数
            s.pop(p)
            p += (m - 1)
        return s[0]


if __name__ == "__main__":
    cls = Solution()
    print(cls.last_remain_solution(5,3))