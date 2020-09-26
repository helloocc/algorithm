#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        该解法易于理解，但最后判断时仅判断root结点是否平衡还不够，还需判断左右子树是否平衡，因此会重复计算子树深度导致效率低。
        """
        def get_depth(node):
            if not node:
                return 0
            depth = max(get_depth(node.left), get_depth(node.right))+1
            return depth

        if not root:
            return True
        return abs(get_depth(root.left)-get_depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)


class Solution2:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        DFS：递归自底向上，判断子树是否平衡，如果不平衡则返回False，无需判断父节点。

        最终返回值可能是num或False。True=1,False=0
        """
        return self.dfs(root) > 0

    def dfs(self, root: TreeNode) -> bool:
        if not root:
            return True
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        if not left or not right or abs(left-right) > 1:
            return False
        return max(left, right)+1


def test1():
    s = Solution1()
    a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(
        20), TreeNode(15), TreeNode(7)
    a.left, a.right = b, c
    c.left, c.right = d, e
    assert s.isBalanced(a) == True


def test2():
    s = Solution1()
    a, b, c, d, e, f, g = TreeNode(1), TreeNode(
        2), TreeNode(3), TreeNode(4), TreeNode(2), TreeNode(3), TreeNode(4)
    a.left, b.left, d.left = b, d, f
    a.right, c.right, e.right = c, e, g
    assert s.isBalanced(a) == False


def test3():
    s = Solution2()
    a, b, c, d, e, f, g = TreeNode(1), TreeNode(
        2), TreeNode(2), TreeNode(3), TreeNode(3), TreeNode(4), TreeNode(4)
    a.left, a.right = b, c
    b.left, b.right = d, e
    d.left, d.right = f, g
    assert s.isBalanced(a) == False


def test4():
    s = Solution2()
    a, b, c = TreeNode(1), TreeNode(
        2), TreeNode(3)
    a.right, b.right = b, c
    assert s.isBalanced(a) == False


def test5():
    s = Solution2()
    a, b, c, d, e = TreeNode(3), TreeNode(9), TreeNode(
        20), TreeNode(15), TreeNode(7)
    a.left, a.right = b, c
    c.left, c.right = d, e
    assert s.isBalanced(a) == True
