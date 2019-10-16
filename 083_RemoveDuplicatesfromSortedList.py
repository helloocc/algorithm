#!/usr/bin/env python
# -*- coding=utf8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        思想：如果next结点与当前结点的值相同，则删除next结点（此时不后移），否则后移一个结点继续判断。
        """
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


def print_node(head: ListNode):
    _str = ''
    while head:
        _str += str(head)
        head = head.next
    return _str


def test1():
    s = Solution()
    a, b, c, d, e = ListNode(1), ListNode(
        1), ListNode(2), ListNode(3), ListNode(3)
    a.next, b.next, c.next, d.next = b, c, d, e
    assert print_node(s.deleteDuplicates(a)) == '123'


def test2():
    s = Solution()
    a, b, c = ListNode(1), ListNode(1), ListNode(2)
    a.next, b.next = b, c
    assert print_node(s.deleteDuplicates(a)) == '12'
