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
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        递归:
        首先判断终止条件。递推公式是交换当前两个节点，而指向下一个节点时已经是交换过的head。
        """
        if not head or not head.next:
            return head

        new_head = head.next

        tmp = self.swapPairs(head.next.next)
        head.next.next = head
        head.next = tmp
        return new_head


def print_node(head: ListNode):
    _str = ''
    while head:
        _str += str(head)
        head = head.next
    return _str


def test1():
    s = Solution()
    a, b, c, d = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
    a.next, b.next, c.next = b, c, d
    assert print_node(s.swapPairs(a)) == '2143'

    e = ListNode(6)
    assert print_node(s.swapPairs(e)) == '6'
