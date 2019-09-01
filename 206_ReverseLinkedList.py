#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        """
        非递归：
        从头结点开始反转，头结点的next变成None，最后一次while循环反转尾结点，之后head变成head.next为None，所以返回pre结点。
        """
        pre = None
        while head:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        return pre

    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归：
        递归到尾结的前一个结点，每次反转当前结点的next结点，next结点指向head，head指向None。
        """
        if (not head) or (not head.next):
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


def print_node(head: ListNode):
    _str = ''
    while head:
        _str += str(head)
        head = head.next
    return _str


def test_reverse():
    s = Solution()
    a, b, c, d = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    a.next, b.next, c.next = b, c, d
    assert print_node(s.reverseList(a)) == '4321'

    e = ListNode(6)
    assert print_node(s.reverseList(e)) == '6'


def test_reverse1():
    s = Solution()
    a, b, c, d = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    a.next, b.next, c.next = b, c, d
    assert print_node(s.reverseList1(a)) == '4321'

    e = ListNode(6)
    assert print_node(s.reverseList1(e)) == '6'
