#!/usr/bin/env python
# -*- coding=utf8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        p, q = headA, headB
        nodes = set()
        while p:
            nodes.add(p)
            p = p.next
        while q:
            if q in nodes:
                return q
            else:
                q = q.next
        return None

    def getIntersectionNode1(self, headA, headB):
        """
        图解示意图：https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49785/Java-solution-without-knowing-the-difference-in-len!/165648

        假设s1 = s1_diff + common，s2 = s2_diff + common
        在第二次迭代后，走过的路径长度为 s1_diff + common + s2_diff = s2_diff + common + s1_diff。此时会同时走到交叉点。
        如果没有任何common部分，则两个指针都将是null。
        """
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p


def test1():
    s = Solution()
    a, b, c, d, e = ListNode(4), ListNode(
        1), ListNode(8), ListNode(4), ListNode(5)
    a.next, b.next, c.next, d.next = b, c, d, e

    f, g, h = ListNode(5), ListNode(0), ListNode(1)

    f.next, g.next, h.next = g, h, c
    assert s.getIntersectionNode(a, f).val == 8


def test2():
    s = Solution()
    a, b, c, d, e = ListNode(0), ListNode(
        9), ListNode(1), ListNode(2), ListNode(4)
    a.next, b.next, c.next, d.next = b, c, d, e

    f = ListNode(3)
    f.next = d
    assert s.getIntersectionNode1(a, f).val == 2


def test3():
    s = Solution()
    a, b, c = ListNode(2), ListNode(6), ListNode(4)
    a.next, b.next = b, c

    f, g = ListNode(1), ListNode(5)
    f.next = g
    assert s.getIntersectionNode1(a, f) == None
