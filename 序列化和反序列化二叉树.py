#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：序列化和反序列化二叉树

题目描述：请实现两个函数，分别用来序列化和反序列化二叉树

解题思路：序列化：把二叉树以某种次序保存到变量或文件中  反序列化：从文件中读取出来构建二叉树
    重点是序列化和反序列化要以相同的遍历次序访问和构建树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Serialize(self, root):
        res = []

        def pre_order(root):
            if not root:
                res.append('#')  # #表示空
            res.append(str(root.val))
            pre_order(root.left)   # 递归遍历左子树
            pre_order(root.right)  # 递归遍历右子树

        pre_order(root)
        return ' '.join(res)  # 以字符串形式返回

    def deserialize(self, s):
        """ s:"'1' '2' '3'以空格间隔的字符串" """
        res = s.split()

        def build_tree():
            """ 前序遍历创建二叉树 """
            if res:
                val = res.pop(0)
                if val == '#':
                    return None
                root = TreeNode(int(val))
                root.left = build_tree()   # 递归创建左子树
                root.right = build_tree()  # 递归创建右子树
                return root
        return build_tree()