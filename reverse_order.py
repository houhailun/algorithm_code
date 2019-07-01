#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目要求：求数组中的逆序对；逆序对是前面数大于后面数，比如(5,2)是一个逆序对

解题思路:
    方法1：两次for循环遍历，比较两个数字是否为逆序对  时间复杂度：O（n*n）
    方法2：利用归并排序的思想，把数组分为若干子数组，先比较子数组内部逆序对，在比较数组间的逆序对
"""


class ReverseOrder(object):
    def __init__(self, array):
        self.array = array
        self.reverse_order_list = []
        self.count = 0

    def reverse_order1(self):
        length = len(self.array)
        count = 0
        for i in range(length):
            for j in range(i+1, length):
                if self.array[i] > self.array[j]:
                    self.reverse_order_list.append((self.array[i], self.array[j]))
                    count += 1
        return count

    def reverse_order2(self, arr):
        # 改写归并排序,在归并排序中，每当R部分元素先于L部分元素插入原列表时，逆序对数要加L剩余元素数
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        lst1 = self.reverse_order2(arr[:mid])
        lst2 = self.reverse_order2(arr[mid:])
        return self.merge(lst1, lst2)

    def merge(self, lst1, lst2):
        i = j = 0
        res = []
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                res.append(lst1[i])
                i += 1
            else:
                res.append(lst2[j])
                self.count += len(lst1) - i  # 当右半部分的元素先于左半部分元素进入有序列表时(左边大右边小)，逆序对数量增加左半部分剩余的元素数
                j += 1

        res += lst1[i:]
        res += lst2[j:]

        return res


if __name__ == "__main__":
    cls = ReverseOrder([1, 2, 3, 4, 5, 6, 7, 0])
    # print(cls.reverse_order1())

    arr = [364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]
    print(cls.reverse_order2(arr))
