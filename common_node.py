#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目要求：输入两个链表，找出它们的第一个公共节点

解题思路：对于求诸如两个链表的公共节点类问题，一般都是设置两个指针，一个先走一个后走，然后相遇即为公共节点
    本题：1、求出两个链表的长度分别为m，n
         2、长的链表先走abs(m-n)步
         3、两个链表一起走，直到相遇，第一个相遇即为所求
"""


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None

        # step1:求两个链表的长度
        len1 = len2 = 0
        pNode1, pNode2 = pHead1, pHead2
        while pNode1:
            len1 += 1
            pNode1 = pNode1.next
        while pNode2:
            len2 += 1
            pNode2 = pNode2.next

        # step2:长的链表先走abs(m-n)步
        if len1 > len2:
            for i in range(len1 - len2):
                pHead1 = pHead1.next
        else:
            for i in range(len2 - len1):
                pHead2 = pHead2.next

        # step3：两个链表一起走
        while pHead1 and pHead2:
            if pHead1 is pHead2:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next

        return None
