#!/usr/bin/env python
#-*- coding=utf8 -*-


class TreeNode:
   def __init__(self, val=0, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        def helper(root, pre):
            """
            展开得到先序遍历的顺序，但按照先序遍历访问，会丢失右子树，按照先序的逆遍历可以解决。
            从右子树开始遍历，返回当前节点作为上一个节点的右子树
            """
            if not root:
                return pre
            pre = helper(root.right, pre)
            pre = helper(root.left, pre)
            root.right = pre
            root.left = None
            pre = root
            return pre

        return helper(root, None)

    def flatten2(self, root: TreeNode) -> None:
        if not root:
            return
        tmp = root.right
        if root.left:
            # 展开左子树
            self.flatten2(root.left)            
            # 找到左子树的tail
            tail = root.left
            while tail.right:
                tail = tail.right              
            # 左子树置空，进行连接
            root.left, root.right, tail.right = None, root.left, tmp
        # 展开右子树
        self.flatten2(tmp)


def test1():
    s = Solution()
    a, b, c = TreeNode(1), TreeNode(2), TreeNode(3)
    a.left, a.right = b, c
    s.flatten(a)
    assert a.right == b
    assert b.right == c

def test2():
    s = Solution()
    a, b = TreeNode(1), TreeNode(2)
    a.left = b
    s.flatten(a)
    assert a.right == b


def test3():
    s = Solution()
    a, b = TreeNode(1), TreeNode(2)
    a.right = b
    s.flatten(a)
    assert a.right == b


def test4():
    s = Solution()
    a, b, c, d, e, f = TreeNode(1), TreeNode(2), TreeNode(
       3), TreeNode(4), TreeNode(5), TreeNode(6)
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.right = f
    s.flatten(a)
    assert a.right == b
    assert b.right == d
    assert d.right == e
    assert e.right == c
    assert c.right == f


def test5():
    s = Solution()
    a, b, c, d, e, f = TreeNode(1), TreeNode(2), TreeNode(
       3), TreeNode(4), TreeNode(5), TreeNode(6)
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.right = f
    s.flatten2(a)
    assert a.right == b
    assert b.right == d
    assert d.right == e
    assert e.right == c
    assert c.right == f
