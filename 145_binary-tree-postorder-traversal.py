#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        """
        递归
        """
        if not root:
            return []
        res = []
        if root.left:
            res += self.postorderTraversal1(root.left)
        if root.right:
            res += self.postorderTraversal1(root.right)
        res.append(root.val)
        return res

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        """
        迭代
        """
        if not root:
            return []
        res = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
            else:
                # postorder add to stack.
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
        return res


def test1():
    a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
    a.right, b.left = b, c
    s = Solution()
    assert s.postorderTraversal1(a) == [3, 2, 1]


def test2():
    a, b = TreeNode(1), TreeNode(2)
    a.left = b
    s = Solution()
    assert s.postorderTraversal2(a) == [2, 1]


def test3():
    a = TreeNode(1)
    s = Solution()
    assert s.postorderTraversal2(a) == [1]
