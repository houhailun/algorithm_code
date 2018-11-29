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
        people = list(range(1, n+1))
        p = 0
        while True:
            if len(people) == 1:
                break
            p = (p + (m-1)) % len(people)  # 更新p
            del people[p]

        return people[0]


if __name__ == "__main__":
    cls = Solution()
    print(cls.last_remain_solution(6,4))