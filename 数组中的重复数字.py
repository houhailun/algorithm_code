#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：数组中重复的数字

题目描述：在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。
        例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

解题思路：1、由于长度为n的数组中的数字都是0到n-1，可以知道排序后如果没有重复必然是0，1，2递增，我们可以检查如果下表和值不同则必然出现重复  缺点:排序需要O(nlogn)时间复杂度
        2、可以利用哈希表来实现，键为数字，值为次数；循环检查是否出现多次  缺点：需要O(n)的辅助空间
        3、数组中的数字都在0到n-1的数字范围内。如果数组中没有重复出现的数字，那么当数组排序后数字i就出现在数组中下标为i的元素处。那么数组中如果存在重复数字的话，有些位置的对应的数字就没有出现，而有些位置可能存在多个数字
           那么我们重排这个数组。从第0个元素开始。
                1、比较numbers[i]和i的值，如果i与numbers[i]相等，也就是对数组排序后，numbers[i]就应该在对应的数组的第i个位置处，那么继续判断下一个位置。
                2、如果i和numbers[i]的值不相等，那么判断以numbers[i]为下标的数组元素是什么。
                    2.1、如果numbers[numbers[i]]等于numbers[i]的话，那么就是说有两个相同的值了，重复了。找到了重复的数字
                    2.2、如果numbers[numbers[i]]不等于numbers[i]的话，那么就将numbers[numbers[i]]和numbers[i]互换。继续进行1的判断。
                3、循环退出的条件是直至数组最后一个元素，仍没有找到重复的数字，数组中不存在重复的数字。  时间复杂度:O(n),不需要额外辅助空间
"""

class Solution:
    def duplicate(self, numbers, duplication):
        if not numbers:
            return False

        numbers.sort()
        for ix, num in enumerate(numbers):
            if ix != num:
                print('ix:%d, num:%d' % (ix, num))
                duplication.append(num)
                return True

        return False

    def duplicate_2(self, numbers, duplication):
        if not numbers:
            return False

        # 利用字段构建哈希表，键为数字，值为次数
        hash_table = {}
        for num in numbers:
            if num in hash_table.keys():
                duplication.append(num)  # duplication[0] = num
                return True
            hash_table[num] = 1
        return False

    def duplicate_3(self, numbers, duplication):
        if not numbers:
            return False

        for ix, num in enumerate(numbers):
            if ix == num:
                continue

            # 判断a[ix] == a[a[ix]],重复
            if numbers[ix] == numbers[numbers[ix]]:
                # duplication[0] = num
                duplication.append(num)
                return False

            # 不重复，交换
            # numbers[ix] = numbers[numbers[ix]] = numbers[numbers[ix]], numbers[ix]  不能用这种方式交换
            tmp = numbers[numbers[ix]]
            numbers[numbers[ix]] = numbers[ix]
            numbers[ix] = tmp
        return False


if __name__ == "__main__":
    cls = Solution()
    ret = []
    cls.duplicate_3([2,1,3,1,4], ret)
    print(ret)