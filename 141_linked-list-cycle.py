#!/usr/bin/env python
# -*- coding=utf8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle1(self, head):
        """
        用set存储node做判断，时间复杂度O(n)，空间复杂度O(n)
        """
        if not head or not head.next:
            return False
        nodes = set()
        while head.next:
            if head.next in nodes:
                return True
            nodes.add(head)
            head = head.next
        return False

    def hasCycle(self, head):
        """
        快慢指针，相遇则有环，时间复杂度O(n)，空间复杂度O(1)

        假设环的长度为R，当慢指针走到环入口时，快指针距离环入口S。
        在慢指针进入环后的t时间内，快指针从S处走了2t个节点，相当于从环入口走了S+2t个节点，而此时慢指针从环入口走了t个节点。
        假设快慢指针一定可以相遇，那么有S+2t−t=nR，即S+t=nR，如果对于任意的S，R，n，总可以找到一个t满足上式，那么就可以说明快慢指针一定可以相遇(显然可以找到)
        而实际上，由于S<R，所以在慢指针走过一圈之前就可以相遇。
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def test1():
    s = Solution()
    a, b, c, d = ListNode(3), ListNode(2), ListNode(0), ListNode(-1)
    a.next, b.next, c.next, d.next = b, c, d, b
    assert s.hasCycle(a)
