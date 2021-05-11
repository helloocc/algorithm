#!/usr/bin/env python
# -*- coding: utf8 -*-


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return

        odd, even = ListNode(), ListNode()
        odd.next, even.next = even, head
        dummy1, dummy2 = odd, even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = odd.next
        odd.next = dummy2.next

        return dummy1.next


def print_node(head):
    _str = ''
    while head:
        _str += str(head.val)
        head = head.next
    return _str


def test1():
    s = Solution()
    a, b, c, d, e = ListNode(1), ListNode(
        2), ListNode(3), ListNode(4), ListNode(5)
    a.next, b.next, c.next, d.next = b, c, d, e
    assert print_node(s.oddEvenList(a)) == '13524'
