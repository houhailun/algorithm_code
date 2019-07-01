#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
丑数定义：质因子为2，3，5的数称为丑数
1是丑数，2，3，5，8是丑数，14不是丑数
"""


class Solution(object):
    def __init__(self, k):
        self.k = k

    def is_ugly(self, num):
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return True if num == 1 else False

    def ugly_1(self):
        """查找第n个丑数"""
        # 暴力法：利用丑数定义 问题：时间复杂度较高，当n较大时所用时间多
        if self.k <= 0:
            return None
        count = 0
        num = 0
        while count < self.k:
            num += 1
            if self.is_ugly(num):
                count += 1
        return num

    def ugly_2(self):
        """
        丑数只包含质因子2，3，5，假设我们已经有n-1个丑数，按照顺序排列，且第n-1的丑数为M。那么第n个丑数一定是由这n-1个丑数分别乘以2，3，5，得到的所有大于M的结果中，最小的那个数。
        事实上我们不需要每次都计算前面所有丑数乘以2，3，5的结果，然后再比较大小。
        因为在已存在的丑数中，一定存在某个数T2，在它之前的所有数乘以2都小于M，而T2×2的结果一定大于M，同理，也存在这样的数T3，T3，T5， 我们只需要标记这三个数即可
        """
        if self.k <= 0:
            return None
        base_list = [1]
        count = 1
        min2 = min3 = min5 = 0
        while count < self.k:
            min_num = min(base_list[min2]*2, base_list[min3]*3, base_list[min5]*5)
            base_list.append(min_num)

            # 更新min2，min3，min5
            while base_list[min2] * 2 <= min_num:
                min2 += 1
            while base_list[min3] * 3 <= min_num:
                min3 += 1
            while base_list[min5] * 5 <= min_num:
                min5 += 1

            count += 1

        return base_list[-1]


if __name__ == "__main__":
    ugly = Solution(5)
    print(ugly.ugly_1())

    print(ugly.ugly_2())