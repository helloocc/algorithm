#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def levelOrder(self, root: TreeNode) -> list:
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, node: TreeNode, level: int, res: list):
        """
        DFS：节点所在的层数与res的索引值相当，加入到层数所在的索引值列表即可。
        """
        if not node:
            return
        if len(res) < level + 1:  # 初始化当前层数的list
            res.append([])
        res[level].append(node.val)
        self.dfs(node.left, level+1, res)
        self.dfs(node.right, level+1, res)


class Solution2:
    def levelOrder(self, root: TreeNode) -> list:
        """
        BFS:使用队列进行bfs.
        """
        res = []
        if not root:
            return res
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if not node:
                continue
            if len(res) < level + 1:  # 初始化当前层数的list
                res.append([])
            res[level].append(node.val)
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
        return res


def test1():
    s = Solution1()
    a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(
        20), TreeNode(15), TreeNode(7)
    a.left, a.right = b, c
    c.left, c.right = d, e
    assert s.levelOrder(a) == [[3], [9, 20], [15, 7]]


def test2():
    s = Solution2()
    a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(
        20), TreeNode(15), TreeNode(7)
    a.left, a.right = b, c
    c.left, c.right = d, e
    assert s.levelOrder(a) == [[3], [9, 20], [15, 7]]
