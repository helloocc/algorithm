#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    通过循环遍历[1，n]创建根节点，以递归方式生成所有可能的子树；
    根据BST的规则，左子树中的所有值均小于根，右子树中的所有值都大于根；
    对于左右子树的每个组合，将它们附加到当前根节点以形成唯一的BST。
    """

    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(l, r):
            if l > r:
                return [None]
            res = []
            for i in range(l, r+1):
                for ltree in generate(l, i-1):
                    for rtree in generate(i+1, r):
                        node = TreeNode(i)
                        node.left, node.right = ltree, rtree
                        res.append(node)
            return res

        return generate(1, n)


def print_tree(trees: List[TreeNode]):
    res = []
    for node in trees:
        values = []
        queue = [node]
        while queue:
            node = queue.pop(0)
            if node:
                values.append(node.val)
                if node.left or node.right:
                    queue.append(node.left)
                    queue.append(node.right)
            else:
                values.append(None)
        if not values[-1]:
            values.pop(-1)

        res.append(values)
    return res


def test1():
    s = Solution()
    res = [[1]]
    assert print_tree(s.generateTrees(1)) == res


def test2():
    s = Solution()
    res = [[1, None, 2, None, 3],
           [1, None, 3, 2],
           [2, 1, 3],
           [3, 1, None, None, 2],
           [3, 2, None, 1]]
    assert print_tree(s.generateTrees(3)) == res
