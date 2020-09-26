#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
         2
       /   \
      1     4
           / \
          3   5
    """

    def isValidBST1(self, root: TreeNode) -> bool:
        """
        递归：判断左子树是否小于root值，右子树是否大于root值。
        """
        def is_valid(root: TreeNode, min_val=float('-inf'), max_val=float('inf')) -> bool:
            if not root:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            return is_valid(root.left, min_val, root.val) and is_valid(root.right, root.val, max_val)

        return is_valid(root)

    def isValidBST2(self, root: TreeNode) -> bool:
        """
        如果是有效的二叉搜索树，则中序遍历后的结果应该是递增序列。
        """
        nums = []

        def inorderTraverse(root: TreeNode):
            if not root:
                return
            inorderTraverse(root.left)
            nums.append(root.val)
            inorderTraverse(root.right)

        inorderTraverse(root)
        return sorted(nums) == nums and len(set(nums)) == len(nums)


def test1():
    s = Solution()
    a, b, c = TreeNode(2), TreeNode(1),  TreeNode(3)
    a.left, a.right = b, c
    assert s.isValidBST1(a) == True


def test2():
    s = Solution()
    a, b, c = TreeNode(1), TreeNode(2),  TreeNode(3)
    a.left, a.right = b, c
    assert s.isValidBST1(a) == False


def test3():
    s = Solution()
    a, b, c, d, e = TreeNode(5), TreeNode(1), TreeNode(
        4), TreeNode(3), TreeNode(6)
    a.left, a.right = b, c
    c.left, c.right = d, e
    assert s.isValidBST1(a) == False


def test4():
    s = Solution()
    a, b, c, d, e = TreeNode(2), TreeNode(1), TreeNode(
        4), TreeNode(3), TreeNode(6)
    a.left, a.right = b, c
    c.left, c.right = d, e
    assert s.isValidBST2(a) == True


def test5():
    s = Solution()
    a, b, c, d, e = TreeNode(3), TreeNode(1), TreeNode(
        4), TreeNode(2), TreeNode(6)
    a.left, a.right = b, c
    c.left, c.right = d, e
    assert s.isValidBST2(a) == False


def test6():
    s = Solution()
    a, b = TreeNode(1), TreeNode(1)
    a.left = b
    assert s.isValidBST2(a) == False
