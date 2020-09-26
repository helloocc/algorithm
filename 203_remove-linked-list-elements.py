#!/usr/bin/env python
# -*- coding=utf8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        """
        非递归：建立dummy node简化场景。
        注意：如果移除cur.next的结点，则cur不后移，因为此时的cur.next已经是新结点。
        """
        if not head:
            return head
        dummy = cur = ListNode(None)
        dummy.next = cur.next = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next

    def removeElements1(self, head: ListNode, val: int) -> ListNode:
        """
        递归：嵌套太深，此题建议非递归法解决。
        """
        if not head:
            return None
        head.next = self.removeElements1(head.next, val)
        return head.next if head.val == val else head


def print_node(head: ListNode):
    _str = ''
    while head:
        _str += str(head)
        head = head.next
    return _str


def test1():
    s = Solution()

    a, b, c, d, e, f = ListNode(1), ListNode(2), ListNode(
        3), ListNode(4), ListNode(5), ListNode(6)
    a.next, b.next, c.next, d.next, e.next = b, c, d, e, f
    assert print_node(s.removeElements(a, 6)) == '12345'
    assert print_node(s.removeElements(a, 3)) == '1245'
    assert print_node(s.removeElements(a, 1)) == '245'

    g, h = ListNode(1), ListNode(1)
    g.next = h
    assert print_node(s.removeElements(g, 1)) == ''


def test2():
    s = Solution()

    a, b, c, d, e, f = ListNode(1), ListNode(2), ListNode(
        3), ListNode(4), ListNode(5), ListNode(6)
    a.next, b.next, c.next, d.next, e.next = b, c, d, e, f
    assert print_node(s.removeElements1(a, 6)) == '12345'
    assert print_node(s.removeElements1(a, 3)) == '1245'
    assert print_node(s.removeElements1(a, 1)) == '245'

    g, h = ListNode(1), ListNode(1)
    g.next = h
    assert print_node(s.removeElements1(g, 1)) == ''
