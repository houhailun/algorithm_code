#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：按之字形顺序打印二叉树

题目描述：请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

解题思路：本题属于层次遍历的变形，奇数层从左到右打印，偶数层从右到左打印；设置两个栈，一个栈存储奇数层数据，另一个存储偶数层数据
    当前层奇数层时：根据左孩子-右孩子顺序入栈2
    当前层偶数层时：根据右孩子-左孩子顺序入栈1，直到两个栈都为空为止
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def print(self, pRoot):
        if not pRoot:
            return None

        stack1, stack2 = [], []
        ret = []
        stack1.append(pRoot)
        while stack1 or stack2:
            while stack1:  # 奇数层，入栈2
                node = stack1.pop()
                tmp.append(node.val)
                if node.left:
                    stack2.append(node.left)
                if node.right:
                    stack2.append(node.right)
            if tmp:
                ret.append(tmp)

            tmp = []
            while stack2:  # 偶数层，入栈1
                node = stack2.pop()
                tmp.append(node.val)
                if node.right:
                    stack1.append(node.right)
                if node.left:
                    stack1.append(node.left)
            if tmp:
                ret.append(tmp)

        return ret