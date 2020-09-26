#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        思想:如果左子树是右子树的镜像，则树是对称的。
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        """
        递归法：判断左子树和右子树是否为镜像。
            终止条件：镜像左和镜像右都为空时，返回True，否则返回False
            递归：左子树的根节点等于右子树的根节点，子树互为镜像。
        """
        if not t1 or not t2:
            return t1 == t2
        return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)


class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        遍历：类似BFS，每次将左右两边对称的节点加入队列中进行比较。
        """
        if not root:
            return True
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop()
            if l and r and l.val == r.val:
                stack.append([l.left, r.right])
                stack.append([l.right, r.left])
            elif not l and not r:
                continue
            else:
                return False
        return True


def test1():
    s = Solution1()
    a, b, c, d, e, f, g = TreeNode(1), TreeNode(2), TreeNode(
        2), TreeNode(3), TreeNode(4), TreeNode(4), TreeNode(3)
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    assert s.isSymmetric(a) == True


def test2():
    s = Solution1()
    a, b, c, d, e = TreeNode(1), TreeNode(
        2), TreeNode(2), TreeNode(3), TreeNode(3)
    a.left, a.right = b, c
    b.right = d
    c.right = e
    assert s.isSymmetric(a) == False


def test3():
    s = Solution1()
    a, b, c, d, e = TreeNode(1), TreeNode(
        2), TreeNode(2), TreeNode(3), TreeNode(3)
    a.left, a.right = b, c
    b.left = d
    c.right = e
    assert s.isSymmetric(a) == True


def test4():
    s = Solution2()
    a, b, c, d, e, f, g = TreeNode(1), TreeNode(2), TreeNode(
        2), TreeNode(3), TreeNode(4), TreeNode(4), TreeNode(3)
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    assert s.isSymmetric(a) == True


def test5():
    s = Solution2()
    a, b, c, d, e = TreeNode(1), TreeNode(
        2), TreeNode(2), TreeNode(3), TreeNode(3)
    a.left, a.right = b, c
    b.right = d
    c.right = e
    assert s.isSymmetric(a) == False


def test6():
    s = Solution2()
    a, b, c, d, e, f, g = TreeNode(1), TreeNode(2), TreeNode(
        2), TreeNode(3), TreeNode(4), None, TreeNode(3)
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.left, c.right = f, g
    assert s.isSymmetric(a) == False
