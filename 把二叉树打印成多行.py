#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
题目：把二叉树打印成多行

题目描述：从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

解题思路：本题就是层次遍历，利用队列实现
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def print(self, pRoot):
        """返回二维列表[[1,2],[4,5]]"""
        if not pRoot:
            return []
        ret, queue = [], []
        queue.append(pRoot)
        while queue:
            tmp = []
            for i in queue:
                tmp.append(i.val)
            ret.append(tmp)

            for i in range(len(queue)):
                node = queue.pop(0)  # pop(0)把队列的头部元素pop
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ret