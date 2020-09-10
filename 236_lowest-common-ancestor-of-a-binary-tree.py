#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode):
        """
        两个节点 p,q 分为两种情况：
        1. p和q在相同子树中
        2. p和q在不同子树中

        DFS遍历，终止条件是节点为空或者遇到p/q
        1. 左右子树返回值都不为空，表明p和q在不同子树中，则当前节点为LCA
        2. 只有一个子树返回值不为空，则该子树的返回值为LCA
        """

        if not root:
            return
        if p == root or q == root:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right


def test1():
    s = Solution()
    a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
    a.left, a.right = b, c
    assert s.lowestCommonAncestor(a, b, c) == a


def test2():
    s = Solution()
    a, b, c, d, e = TreeNode(1), TreeNode(
        2), TreeNode(3), TreeNode(4), TreeNode(5)
    a.left, a.right = b, c
    b.left, c.right = d, e
    assert s.lowestCommonAncestor(a, d, e) == a


def test3():
    s = Solution()
    a, b, c, d, e, f, g, h, i = TreeNode(3), TreeNode(5), TreeNode(1), TreeNode(
        6), TreeNode(2), TreeNode(0), TreeNode(8), TreeNode(7), TreeNode(4)
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    e.left, e.right = h, i
    assert s.lowestCommonAncestor(a, b, c) == a


def test4():
    s = Solution()
    a, b, c, d, e, f, g, h, i = TreeNode(3), TreeNode(5), TreeNode(1), TreeNode(
        6), TreeNode(2), TreeNode(0), TreeNode(8), TreeNode(7), TreeNode(4)
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    e.left, e.right = h, i
    assert s.lowestCommonAncestor(a, b, i) == b
