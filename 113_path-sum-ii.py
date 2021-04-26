#!/usr/bin/env python
# -*- coding: utf8 -*-
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []

        def dfs(node, remain, path):
            if not node:
                return
            if not node.left and not node.right and node.val == remain:
                res.append(path + [node.val])
            dfs(node.left, remain - node.val, path + [node.val])
            dfs(node.right, remain - node.val, path + [node.val])
            return res

        return dfs(root, sum, [])


def test1():
    a, b, c, d, e, f, g, h, i, j = (
        TreeNode(5),
        TreeNode(4),
        TreeNode(8),
        TreeNode(11),
        TreeNode(13),
        TreeNode(4),
        TreeNode(7),
        TreeNode(2),
        TreeNode(5),
        TreeNode(1))
    a.left, a.right = b, c
    b.left = d
    c.left, c.right = e, f
    d.left, d.right = g, h
    f.left, f.right = i, j
    s = Solution()
    assert s.pathSum(a, 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]


def test2():
    a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
    a.left, a.right = b, c
    s = Solution()
    assert s.pathSum(a, 5) == []


def test3():
    a, b = TreeNode(1), TreeNode(2)
    a.left = b
    s = Solution()
    assert s.pathSum(a, 0) == []


def test4():
    a, b = TreeNode(-2), TreeNode(-3)
    a.left = b
    s = Solution()
    assert s.pathSum(a, -5) == [[-2, -3]]
