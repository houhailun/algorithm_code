#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目说明：输入一颗二叉树，判断是否是平衡二叉树

题目解释：平衡二叉树：左右子树深度相差不超过1，且左右子树也是平衡二叉树

解题思路：本体和求树的深度类似，都是需要求左右子树的深度，本题需要添加限制条件：左右子树深度相差不超过1
"""


class Solution:
    def is_balance_tree(self, tree):
        # 遍历每个结点，借助一个获取树深度的递归函数，根据该结点的左右子树高度差判断是否平衡，然后递归地对左右子树进行判断
        if not tree:
            return True

        left = self.max_depth(tree.left)
        right = self.max_depth(tree.right)

        if left-right > 1 or right-left > 1:
            return False

        return self.is_balance_tree(tree.left) and self.is_balance_tree(tree.right)

    def max_depth(self, tree):
        if not tree:
            return 0

        left = self.max_depth(tree.left)
        right = self.max_depth(tree.right)
        return max(left, right) + 1

    def is_balance_tree_2(self, tree):
        # 上面的方法有个缺点是先从上面的节点依次检查子树深度，然后递归往下继续判断，造成很多结点重复判断深度
        # 这里可以:从下往上检查，如果子树是平衡二叉树，返回子树的深度，如果子树不是平衡二叉树则直接返回false
        return self.get_depth(tree) != -1

    def get_depth(self, tree):
        if tree is None:
            return 0
        # 左右子树深度
        left = self.get_depth(tree.left)
        right = self.get_depth(tree.right)

        # 左右子树不平衡则直接返回-1
        if left == -1:
            return -1
        if right == -1:
            return -1

        # 左右子树深度差是否为1
        return -1 if(abs(left-right)>1) else 0
