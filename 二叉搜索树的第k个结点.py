#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：二叉搜索树的第k个结点

题目描述：给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。

解题思路：二叉搜索树是一种特殊的二叉树L:左子树结点值小于根结点值；右子树结点值大于根节点值；中序遍历（左-根-右）即可得到有序数组
    方法1：对二叉搜索树中序遍历后得到有序数组，通过索引即可获取第k个结点值  时间复杂度:O(N*logN)  空间复杂度:O(N)
    方法2：不需要对整个树遍历，只需要遍历到第k个结点后停止即可
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kth_node(self, pRoot, k):
        if not pRoot or k == 0:
            return None
        res = []

        def in_order(root):
            # 中序遍历获得有序序列
            if not root:
                return None
            in_order(root.left)
            res.append(root)
            in_order(root.right)

        in_order(pRoot)
        if k > len(res):
            return None
        return res[k-1]  # 下标是从0开始

    def kth_node_2(self, pRoot, k):
        if not pRoot or k == 0:
            return None
        index = 0

        def kth_helper(root, k):
            if not root:
                return None
            # 递归左子树，并判断有无返回节点。如果有，停止递归，返回所要返回的节点
            node = kth_helper(root.left, k)
            if node:
                return node
            # 当左子树没有返回节点时，判断当前的根节点是不是第k个遍历到的值（即第k大）。如果是，则返回该节点，停止递归
            nonlocal index  # python3中修改外部变量需要指定nonlocal或者global，list不需要
            index += 1
            if index == k:
                return root
            # 当左子树和根节点都没有返回节点时，递归右子树，并判断有无返回节点。如果有，停止递归，返回所要返回的节点。
            node = kth_helper(root.right, k)
            if node:
                return node
        return kth_helper(pRoot, k)

