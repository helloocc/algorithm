#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        递归
        """
        if not root:
            return []
        res = []
        res.append(root.val)
        if root.left:
            res += self.preorderTraversal1(root.left)
        if root.right:
            res += self.preorderTraversal1(root.right)
        return res

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        迭代
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


def test1():
    a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
    a.right, b.left = b, c
    s = Solution()
    assert s.preorderTraversal1(a) == [1, 2, 3]


def test2():
    a, b = TreeNode(1), TreeNode(2)
    a.left = b
    s = Solution()
    assert s.preorderTraversal2(a) == [1, 2]


def test3():
    a = TreeNode(1)
    s = Solution()
    assert s.preorderTraversal2(a) == [1]
