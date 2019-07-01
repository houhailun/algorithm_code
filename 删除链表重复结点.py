#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目: 删除链表中重复的结点

题目描述: 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

解题思路: 假设链表是有序的，两个指针p1,p2,p1指向前一个节点，p2指向后一个节点
    1、p2.val != p2.next.val：p1，p2指针后移
    2、p2.val == p2.next.val：p2后移直到不是重复元素节点为止,p1.next=p2
    注意：由于第一个节点可能是重复元素，需要添加指向第一个节点的头节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_duplication(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead

        # 由于第一个结点有可能是重复结点，因此需要加一个指向第一个结点的头节点
        first_node = ListNode(-1)
        first_node.next = pHead

        curr = pHead        # 指向当前结点
        last = first_node   # 上一结点指针
        while curr and curr.next:
            if curr.val != curr.next.val:  # 不重复，后移
                curr = curr.next
                last = last.next
            else:
                val = curr.val
                # 找到下一个不重复的结点
                while curr and curr.val == val:
                    curr = curr.next
                last.next = curr
        return first_node.next
