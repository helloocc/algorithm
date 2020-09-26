#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        逆向思维：无需计算总路径的值，每次减当前结点的值，到叶结点时应该与sum值相等。
        """
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True

        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


def test1():
    s = Solution()
    a, b, c, d, e, f, g, h, i = TreeNode(1), TreeNode(4), TreeNode(8), TreeNode(
        11), TreeNode(13), TreeNode(4), TreeNode(7), TreeNode(2), TreeNode(1)
    a.left, a.right = b, c
    b.left = d
    c.left, c.right = e, f
    d.left, d.right = g, h
    f.right = i
    assert s.hasPathSum(a, 22) == True
