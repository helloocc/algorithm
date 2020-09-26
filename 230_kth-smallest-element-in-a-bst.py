#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    中序遍历就是按从小到大排序
    """

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = k
        self.ret = 0

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.count -= 1
            if not self.count:
                self.ret = node.val
                return
            dfs(node.right)

        dfs(root)
        return self.ret


def test1():
    s = Solution()
    a, b, c, d = TreeNode(3), TreeNode(1), TreeNode(4), TreeNode(2)
    a.left, a.right = b, c
    b.right = d
    assert s.kthSmallest(a, 1) == 1


def test2():
    s = Solution()
    a, b, c, d, e, f = TreeNode(5), TreeNode(3), TreeNode(
        6), TreeNode(2), TreeNode(4), TreeNode(1)
    a.left, a.right = b, c
    b.left, b.right = d, e
    d.left = f
    assert s.kthSmallest(a, 3) == 3
