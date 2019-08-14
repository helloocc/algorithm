#!/usr/bin/env python
# -*- coding=utf8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        非递归：生成哨兵结点。每次比较l1和l2的大小，新head每次指向值比较小的结点。
        """
        dummy_node = current = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 or l2
        return dummy_node.next

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        递归：递归比较下一个结点和另一方结点。
        """
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


def print_node(head: ListNode):
    _str = ''
    while head:
        _str += str(head)
        head = head.next
    return _str


def test1():
    s = Solution()

    a, b, c = ListNode(1), ListNode(2), ListNode(4)
    a.next, b.next, = b, c
    d, e, f = ListNode(1), ListNode(3), ListNode(4)
    d.next, e.next, = e, f
    assert print_node(s.mergeTwoLists1(a, d)) == '112344'

    a = ListNode(1)
    d = ListNode(2)
    assert print_node(s.mergeTwoLists1(a, d)) == '12'


def test2():
    s = Solution()

    a, b, c = ListNode(1), ListNode(2), ListNode(4)
    a.next, b.next, = b, c
    d, e, f = ListNode(1), ListNode(3), ListNode(4)
    d.next, e.next, = e, f
    assert print_node(s.mergeTwoLists(a, d)) == '112344'

    a = ListNode(1)
    d = ListNode(2)
    assert print_node(s.mergeTwoLists(a, d)) == '12'
