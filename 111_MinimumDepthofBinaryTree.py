#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
        递归：注意审题是求根节点到叶子节点的最小深度。
        """
        if not root:
            return 0
        if not root.left or not root.right:  # 特殊场景，不能简单求最小
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.left), self.minDepth(root.right))+1


def test1():
    s = Solution()
    a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(
        20), TreeNode(15), TreeNode(7)
    a.left, a.right = b, c
    c.left, c.right = d, e
    assert s.minDepth(a) == 2


def test2():
    s = Solution()
    a, b = TreeNode(3), TreeNode(9)
    a.right = b
    assert s.minDepth(a) == 2
