#!/usr/bin/env python
# -*- coding=utf8 -*-


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.random = None


class Solution:
    def copyRandomList1(self, head: Node) -> Node:
        """
        使用dict记录
        """
        if not head:
            return

        memo = dict()
        origin = head
        while head:
            memo[head] = Node(head.val)
            head = head.next

        head = origin
        while head:
            if head.next:
                memo[head].next = memo[head.next]
            if head.random:
                memo[head].random = memo[head.random]
            head = head.next

        return memo[origin]

    def copyRandomList2(self, head: Node) -> Node:
        if not head:
            return

        origin = head
        # 在原结点后复制一个新结点
        while head:
            new = Node(head.val)
            new.next = head.next
            head.next = new
            head = new.next

        # 设置新结点random
        head = origin
        while head:
            if head.random:
                # 新结点的random是老结点random的下一个（原random结点被复制）
                head.next.random = head.random.next
            head = head.next.next

        # 拆分新旧链表
        head = origin
        new = cur = Node(0)
        while head:
            cur.next = head.next
            cur = cur.next
            head.next = head.next.next
            head = head.next

        return new.next


def print_node(head):
    _str = ''
    while head:
        _str += str(head.val)
        if head.random:
            _str += str(head.random.val)
        head = head.next
    return _str


def test1():
    a, b, c, d, e = Node(7), Node(13), Node(11), Node(10), Node(1)
    a.next, b.next, c.next, d.next = b, c, d, e
    b.random, c.random, d.random = a, e, c
    s = Solution()
    assert print_node(s.copyRandomList1(a)) == '713711110111'
    assert print_node(s.copyRandomList2(a)) == '713711110111'
