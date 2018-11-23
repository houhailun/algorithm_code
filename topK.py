#!/usr/bin/env python
# -*- coding:utf-8 -*-

import heapq

"""
TopK问题：查找最大的K个数和最小的K个数
方法：1、partition方法
     2、最大堆、最小堆
"""

def partition(arr, low, high):
    key = arr[low]
    while low < high:
        while low < high and arr[high] >= key:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= key:
            low += 1
        arr[high] = arr[low]
    arr[low] = key
    return low


def top_K(tinput, k):
    if tinput is None or k > len(tinput) or k <= 0:
        return
    index = partition(tinput, 0, len(tinput) - 1)
    while index != k-1:
        if index < k-1:
            print("tinput: ", tinput)
            print("index:", index)
            index = partition(tinput, index + 1, len(tinput) - 1)
        if index > k-1:
            index = partition(tinput, 0, index - 1)

    return tinput[:k]


def head(tinput, k):
    length = len(tinput)
    ix = length // 2
    while ix >= 0:
        heap_adjust(tinput, ix, length - 1)
        ix -= 1
    print("tinput: ", tinput)

    res = []
    for j in range(length - 1, length - k - 1, -1):
        res.append(tinput[0])
        tinput[0] = tinput[j]
        heap_adjust(tinput, 0, j)
    return res


def heap_adjust(arr, start, end):
    tmp = arr[start]
    i = start * 2  # start节点的左右子孩子节点
    while i <= end:
        if i < end and arr[i] > arr[i + 1]:  # 找到左右子孩子中的大值
            i += 1
        if arr[i] >= tmp:
            break
        arr[i], arr[start] = arr[start], arr[i]  # 交换父节点和左右子孩子的大值
        start = i  # 递归往下执行
        i *= 2
    arr[start] = tmp


class TopKMaxHeap:
    """利用heapq模块，实现大数据情况的topK问题"""
    def __init__(self, k):
        self.data = []
        self.k = k

    def push(self, elem):
        if len(self.data) < self.k:
            heapq.heappush(self.data, elem)  # 入堆
        else:
            top_small = self.data[0]  # 最小值
            if top_small < elem:
                heapq.heapreplace(self.data, elem)  # 弹出并返回最小值，然后将heapqreplace方法中item的值插入到堆中

    def topK(self):
        return [x for x in reversed([heapq.heappop(self.data) for x in range(len(self.data))])]  # 从最大开始显示


class TopKMinHeap:
    """
    大数据情况下，最小的topK问题
    """
    def __init__(self, k):
        self.data = []
        self.k = k

    def push(self, elem):
        if len(self.data) < self.k:
            heapq.heappush(self.data, -elem)  # 注意：这里压入的是-elem
        else:
            small_large = self.data[0]  # 当前最小堆中的最大值
            if -elem > small_large:
                heapq.heapreplace(self.data, -elem)

    def topK(self):
        # 由于入堆是取负数，这里出堆同样负数，并且按照最小的在前
        return [x for x in reversed([-heapq.heappop(self.data) for x in range(len(self.data))])]


if __name__ == "__main__":
    arr = [4,5,1,6,2,7,3,8]
    # print(head(arr, 4))
    list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    th = TopKMaxHeap(5)
    for i in list_num:
        th.push(i)
    print(th.topK())

    th = TopKMinHeap(5)
    for i in list_num:
        th.push(i)
    print(th.topK())