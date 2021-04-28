#!/usr/bin/env python
# -*- coding: utf8 -*-
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers1(self, root: TreeNode) -> int:
        """
        递归记录每条path，最后结算
        """
        res = []

        def dfs(node, count):
            if not node:
                return
            count = count * 10 + node.val if count else node.val
            if not node.left and not node.right:
                res.append(count)
                return
            dfs(node.left, count)
            dfs(node.right, count)
            return res

        dfs(root, 0)
        return sum(res)

    def sumNumbers2(self, root: TreeNode) -> int:
        """
        利用队列，每次将当前结点及其sum入队
        """
        res = 0
        queue = deque()
        queue.append((root, root.val))
        while queue:
            node, val = queue.popleft()
            if not node.left and not node.right:
                res += val
            if node.left:
                queue.append((node.left, val * 10 + node.left.val))
            if node.right:
                queue.append((node.right, val * 10 + node.right.val))
        return res


def test1():
    a, b, c, d, e = (
        TreeNode(4),
        TreeNode(9),
        TreeNode(0),
        TreeNode(5),
        TreeNode(1))
    a.left, a.right = b, c
    b.left, b.right = d, e
    s = Solution()
    assert s.sumNumbers1(a) == 1026
    assert s.sumNumbers2(a) == 1026


def test2():
    a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
    a.left, a.right = b, c
    s = Solution()
    assert s.sumNumbers1(a) == 25
    assert s.sumNumbers2(a) == 25
