#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目说明：输入一颗二叉树，求树的深度
深度定义：从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度

解题思路：
    递归法：由于是从根节点出发，因此可用树的前序遍历，树的深度等于左右子树深度的大值+1
    循环法：利用层次遍历
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0

        # 树深度为左右子树深度的大值+1
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left, right)+1

    def TreeDepth_v2(self, pRoot):
        if not pRoot:
            return 0
        return self.tree_depth(pRoot)

    def tree_depth(self, tree):
        q = list()
        q.append(tree)
        count = 0
        while len(q) != 0:
            length = len(q)
            for i in range(length):  # 每次pop一层node
                node = q.pop()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            count += 1

        return count