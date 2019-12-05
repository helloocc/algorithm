#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        """
        递归: 先找出root结点，再递归找出左右子树。
        """
        if not nums:
            return
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


def inordertraversal(root: TreeNode) -> list:
    def traversal(root: TreeNode):
        if not root:
            return []
        return traversal(root.left)+[root.val]+traversal(root.right)
    return traversal(root)


def test1():
    s = Solution()
    nums = [-10, -3, 0, 5, 9]
    x = s.sortedArrayToBST(nums)
    assert inordertraversal(x) == nums


def test2():
    s = Solution()
    nums = [1, 2, 3]
    x = s.sortedArrayToBST(nums)
    assert inordertraversal(x) == nums
