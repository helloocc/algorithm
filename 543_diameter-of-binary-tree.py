#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        二叉树的直径是树中任意两个结点之间的最长路径的长度。不一定会通过根结点。
        """
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            # 每次比较最长路径
            self.res = max(self.res, left + right)
            # 返回最大深度
            return max(left, right) + 1

        dfs(root)
        return self.res


def test1():
    a, b, c, d, e = TreeNode(1), TreeNode(
        2), TreeNode(3), TreeNode(4), TreeNode(5)
    a.left, a.right = b, c
    b.left, b.right = d, e
    s = Solution()
    assert s.diameterOfBinaryTree(a) == 3
