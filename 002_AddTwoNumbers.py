#!/usr/bin/env python
# -*- coding=utf8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        先遍历生成int,求值后再生成链表。
        """
        s1, s2 = '', ''
        while l1:
            s1 = s1 + str(l1.val)
            l1 = l1.next
        while l2:
            s2 = s2 + str(l2.val)
            l2 = l2.next

        num = int(s1[::-1])+int(s2[::-1])
        num = str(num)[::-1]
        pivot = head = ListNode(num[0])
        for x in num[1:]:
            head.next = ListNode(int(x))
            head = head.next
        return pivot

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        内置函数divmod()
        x,y = divmod(m,n)
        x = m//n
        y = m%n
        """
        carry = 0
        pivot = head = ListNode(0)
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)
            head.next = ListNode(val)
            head = head.next
        return pivot.next


def print_node(head: ListNode):
    _str = ''
    while head:
        _str += str(head.val)
        head = head.next
    return _str


def test1():
    s = Solution()
    a, b, c = ListNode(2), ListNode(4), ListNode(3)
    a.next, b.next, = b, c
    d, e, f = ListNode(5), ListNode(6), ListNode(4)
    d.next, e.next, = e, f
    assert print_node(s.addTwoNumbers1(a, d)) == '708'

    a, b, c = ListNode(1), ListNode(4), ListNode(3)
    a.next, b.next, = b, c
    d, e = ListNode(7), ListNode(9)
    d.next = e
    assert print_node(s.addTwoNumbers1(a, d)) == '834'


def test2():
    s = Solution()
    a, b, c = ListNode(2), ListNode(4), ListNode(3)
    a.next, b.next, = b, c
    d, e, f = ListNode(5), ListNode(6), ListNode(4)
    d.next, e.next, = e, f
    assert print_node(s.addTwoNumbers2(a, d)) == '708'

    a, b, c = ListNode(1), ListNode(4), ListNode(3)
    a.next, b.next, = b, c
    d, e = ListNode(7), ListNode(9)
    d.next = e
    assert print_node(s.addTwoNumbers2(a, d)) == '834'
