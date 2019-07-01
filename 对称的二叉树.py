#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目: 对称的二叉树

题目描述: 请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

解题思路: 1、何为树的镜像：结点的左右子树互换位置
         2、何为对称：和镜像树一样
         3、在不求镜像树的前提下如果判断是否对称：左=右，右=左，即结点的左子树等于其兄弟结点的右子树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot is None:
            return False

        return self.check_tree(pRoot.left, pRoot.right)

    def check_tree(self, left, right):
        if not left and not right:  # 左右子树都遍历完成，是对称树
            return True
        if not left and right:  # 有一个遍历完，另一个没有遍历完，不是对称树
            return False
        if left and not right:
            return False

        if left.val != right.val:  # 左子树节点值不等于右子树节点值，不是对称树
            return False

        left = self.check_tree(left.left, right.right)   # 递归左子树的左子结点和右子树的右子结点
        right = self.check_tree(left.right, right.left)  # 递归左子树的右子结点和右子树的左子结点
        return left and right

    def is_symmetrical_v2(self, root):
        # 迭代实现：类似与层次遍历
        if not root:
            return True
        node_list = [root.left, root.right]
        while node_list:
            left_node = node_list.pop(0)
            right_node = node_list.pop(0)
            if not left_node and not right_node:
                continue
            if not left_node or not right_node:
                return False
            if left_node.val != right_node.val:
                return False

            # 注意插入顺序
            node_list.append(left_node.left)
            node_list.append(right_node.right)
            node_list.append(left_node.right)
            node_list.append(right_node.left)
        return True
