#!/usr/bin/env python
# -*- coding=utf8 -*-


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    归并排序：分治，先拆分再合并
    """

    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # 设置哨兵结点，快慢指针找到mid
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 从中间拆分成两个部分，再递归继续拆分左右
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)

        # 排序并合并
        return self.merge(left, right)

    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        合并两个列表有序链表，参考题解021
        递归的空间复杂度不是常量，所以用迭代法
        """
        dummy = current = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2
        return dummy.next


def print_node(head: ListNode):
    _str = ''
    while head:
        _str += str(head.val)
        head = head.next
    return _str


def test1():
    a, b, c, d = ListNode(4), ListNode(2), ListNode(1), ListNode(3)
    a.next, b.next, c.next = b, c, d
    s = Solution()
    assert print_node(s.sortList(a)) == '1234'


def test2():
    a, b, c, d, e = ListNode(-1), ListNode(
        5), ListNode(3), ListNode(4), ListNode(0)
    a.next, b.next, c.next, d.next = b, c, d, e
    s = Solution()
    assert print_node(s.sortList(a)) == '-10345'
