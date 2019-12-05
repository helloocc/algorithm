#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal1(self, root: TreeNode) -> list:
        """
        递归
        """
        def traversal(root: TreeNode):
            if not root:
                return []
            return traversal(root.left)+[root.val]+traversal(root.right)

        return traversal(root)

    def inorderTraversal2(self, root: TreeNode) -> list:
        """
        非递归：使用栈存储待访问结点。

        先把根节点入栈，如果左子树一直不为空，就一直入栈，直到把所有左节点入栈，然后pop栈顶元素，指针指向栈顶元素的右子树
        """
        res, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

    def inorderTraversal3(self, root: TreeNode) -> list:
        """
        非递归：栈记录每个结点的访问状态。
        """
        res = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not node:
                continue
            if visited:
                res.append(node.val)
            else:
                # 栈先进后出，所以先加right再加left
                stack.append([node.right, False])
                stack.append([node, True])
                stack.append([node.left, False])
        return res


def test1():
    s = Solution()
    a, b, c = TreeNode(2), TreeNode(1),  TreeNode(3)
    a.left, a.right = b, c
    assert s.inorderTraversal1(a) == [1, 2, 3]


def test2():
    s = Solution()
    a, b, c = TreeNode(1), TreeNode(2),  TreeNode(3)
    a.right, b.left = b, c
    assert s.inorderTraversal2(a) == [1, 3, 2]


def test3():
    s = Solution()
    a, b, c, d, e = TreeNode(5), TreeNode(1), TreeNode(
        4), TreeNode(3), TreeNode(6)
    a.left, a.right = b, c
    c.left, c.right = d, e
    assert s.inorderTraversal3(a) == [1, 5, 3, 4, 6]
