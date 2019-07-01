#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
题目：链表中环的入口结点

题目描述：给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null

解题思路：对于找链表公共节点，入口节点等问题可以用两个一快一慢的指针
    方法1：p1每次走一步，p2循环链表，第一个相同的结点就是入口结点  时间复杂度O(N*N)
    方法2：遍历链表，第一个重复的结点就是入口结点  时间复杂度:O（N）  空间复杂度:O(N)
    方法3：假设环中有n个结点，那么p1先走n步，然后两个结点一起走，相遇的结点就是入口结点，问题是如何获取环中结点个数：
        p1每次走1步，p2走两步，相遇的地方就是环中某个结点，此时p1不动，p2循环，可以知道环中的结点个数
"""


class Solution:
    def entry_node_of_loop(self, pHead):
        node = self.meet_nodes(pHead)
        if node is None:
            return None
        # 环中结点数
        slow = node
        cnt = 1
        while slow.next != node:
            cnt += 1
            slow = slow.next

        # fast先走cnt步
        fast = pHead
        for i in range(cnt):
            fast = fast.next

        # 一起走
        slow = pHead
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

    def meet_nodes(self, pHead):
        # 查找环中的结点
        if pHead is None:
            return None
        slow = pHead.next
        if slow is None:
            return None
        fast = slow.next
        while not slow and not fast:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next
            if slow != fast:
                fast = fast.next
        return None