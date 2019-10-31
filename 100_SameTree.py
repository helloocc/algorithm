#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        递归：分别比较结点值和左子树，右子树
        终止条件：被比较的节点都为空则返回True，否则返回False
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q


def test1():
    s = Solution()
    a, b, c, d, e, f = TreeNode(1), TreeNode(2), TreeNode(
        3), TreeNode(1), TreeNode(2), TreeNode(3)
    a.left, a.right = b, c
    d.left, d.right = e, f
    assert s.isSameTree(a, d) == True


def test2():
    s = Solution()
    a, b, c, d = TreeNode(1), TreeNode(
        2), TreeNode(1), TreeNode(2)
    a.left = b
    c.right = d
    assert s.isSameTree(a, c) == False


def test3():
    s = Solution()
    a, b, c, d, e, f = TreeNode(1), TreeNode(2), TreeNode(
        1), TreeNode(1), TreeNode(1), TreeNode(2)
    a.left, a.right = b, c
    d.left, d.right = e, f
    assert s.isSameTree(a, e) == False
