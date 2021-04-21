#!/usr/bin/env python
# -*- coding=utf8 -*-
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        """层次遍历"""
        if not root:
            return []
        res = [root.val]
        queue = deque()
        queue.append((root, 1))
        cur_level = 1
        while queue:
            node, level = queue.popleft()
            # 先加右节点，再加左节点
            if node.right:
                queue.append((node.right, level+1))
            if node.left:
                queue.append((node.left, level+1))
            # 第一次遍历下一层时,当前节点是该层最右的一个
            if level > cur_level:
                res.append(node.val)
                cur_level += 1
        return res


def test1():
    s = Solution()
    a, b, c, d, e = TreeNode(1), TreeNode(
        2), TreeNode(3), TreeNode(5), TreeNode(4)
    a.left, a.right = b, c
    b.right = d
    c.right = e
    res = [1, 3, 4]
    assert s.rightSideView(a) == res


def test2():
    s = Solution()
    a, b = TreeNode(1),  TreeNode(3)
    a.right = b
    res = [1, 3]
    assert s.rightSideView(a) == res


def test3():
    s = Solution()
    a = None
    res = []
    assert s.rightSideView(a) == res
