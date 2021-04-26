#!/usr/bin/env python
# -*- coding: utf8 -*-
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        else:
            return (root.val +
                    self.rangeSumBST(root.left, low, high) +
                    self.rangeSumBST(root.right, low, high))


def test1():
    s = Solution()
    a, b, c, d, e, f = TreeNode(10), TreeNode(5), TreeNode(
        15), TreeNode(3), TreeNode(7), TreeNode(18)
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.right = f
    low, high = 7, 15
    assert s.rangeSumBST(a, low, high) == 32


def test2():
    s = Solution()
    a, b, c, d, e, f, g, h, i = (
        TreeNode(10),
        TreeNode(5),
        TreeNode(15),
        TreeNode(3),
        TreeNode(7),
        TreeNode(13),
        TreeNode(18),
        TreeNode(1),
        TreeNode(6))
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    d.left = h
    e.left = i
    low, high = 6, 10
    assert s.rangeSumBST(a, low, high) == 23
