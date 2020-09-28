#!/usr/bin/env python
# -*- coding=utf8 -*-


class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def connect(self, root: Node) -> Node:
        """
        层次遍历
        """
        if not root:
            return
        queue = [(1, root)]
        while queue:
            level, node = queue.pop(0)
            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))
            if queue and queue[0][0] == level:
                node.next = queue[0][1]
        return root


def test1():
    s = Solution()
    a, b, c = Node(1), Node(2), Node(3)
    a.left, a.right = b, c
    a = s.connect(a)
    assert not a.next
    assert b.next == c


def test2():
    s = Solution()
    a, b, c, d, e, f = Node(1), Node(2), Node(3), Node(4), Node(5), Node(7)
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.right = f
    a = s.connect(a)
    assert not a.next
    assert b.next == c
    assert not c.next
    assert d.next == e
    assert e.next == f
    assert not f.next
