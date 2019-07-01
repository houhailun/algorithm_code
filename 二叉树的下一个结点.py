#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目: 二叉树的下一个结点

题目描述: 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

解题思路: 中序遍历：左-根-右
    方法1：中序遍历二叉后按照便利顺序保存结点，在列表中查找    时间复杂度:O(n)  空间复杂度:O(n)
    方法2：仔细分析可知:
        如果指定结点有右子树，则它下一个结点是右子树的最左子结点
        若果指定结点为其父节点的左孩子，则它下一个结点是其父节点；
        如果指定结点是其父节点的右孩子，则它的下一个结点是其父节点的父节点的父节点...，知道当前结点是其父节点的左孩子
        特殊情况：尾结点没有下一个结点
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None  # 父节点指针


class Solution:
    def GetNext(self, pNode):
        """
        查找二叉树指定结点的下一个结点
        :param pNode: 指定的结点
        :return: 中序遍历的下一个结点
        """
        if pNode is None:
            return None
        if pNode.right:  # 右孩子不为空,下一个结点是右子树的最左结点
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode

        while pNode.next:  # 父节点不为空
            proot = pNode.next
            if proot.left == pNode:  # pNode是父节点左孩子
                return proot
            pNode = pNode.next  # pNode是父节点右孩子