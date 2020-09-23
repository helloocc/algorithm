#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        层次遍历，队列中记录当前层数，通过层数奇偶来判定遍历结果的添加方向。
        """
        queue = [(0, root)]
        res = []
        while queue:
            level, node = queue.pop(0)
            if not node:
                continue
            if len(res) == level:
                res.append([])
            if not level % 2:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)

            queue.append((level + 1, node.left))
            queue.append((level + 1, node.right))
        return res


def test1():
    a, b, c, d, e = TreeNode(3), TreeNode(
        9), TreeNode(20), TreeNode(15), TreeNode(7)
    a.left, a.right = b, c
    c.left, c.right = d, e
    s = Solution()
    assert s.zigzagLevelOrder(a) == [[3], [20, 9], [15, 7]]


def test2():
    a = TreeNode(7)
    s = Solution()
    assert s.zigzagLevelOrder(a) == [[7]]
