#!/usr/bin/env python
# -*- coding=utf8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        引入哨兵结点减少边界场景。
        维持两个指针，当runner跑到尾结点时，current结点在倒数n结点的前一个结点。
        """
        dummy_node = ListNode(None)
        dummy_node.next = head
        current = runner = dummy_node
        while n:
            runner = runner.next
            n -= 1
        while runner.next:
            runner = runner.next
            current = current.next
        current.next = current.next.next
        return dummy_node.next


def print_node(head: ListNode):
    _str = ''
    while head:
        _str += str(head)
        head = head.next
    return _str


def test1():
    s = Solution()
    a, b, c, d, e = ListNode(1), ListNode(
        2), ListNode(3), ListNode(4), ListNode(5)
    a.next, b.next, c.next, d.next = b, c, d, e
    assert print_node(s.removeNthFromEnd(a, 1)) == '1234'


def test2():
    s = Solution()
    t1, t2 = ListNode(1), ListNode(2)
    t1.next = t2
    assert print_node(s.removeNthFromEnd(t1, 2)) == '2'


def test3():
    s = Solution()
    t3 = ListNode(1)
    assert print_node(s.removeNthFromEnd(t3, 1)) == ''
