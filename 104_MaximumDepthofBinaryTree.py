#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """
        递归：最大深度是左右子树的最大值+1
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def test1():
    s = Solution()
    a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(
        20), TreeNode(15), TreeNode(7)
    a.left, a.right = b, c
    c.left, c.right = d, e
    assert s.maxDepth(a) == 3


def test2():
    s = Solution()
    a = TreeNode(1)
    assert s.maxDepth(a) == 1
