#!/usr/bin/env python
#-*- coding=utf8 -*-

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return
        root = TreeNode(preorder.pop(0))
        sp = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:sp])
        root.right = self.buildTree(preorder, inorder[sp+1:])
        return root



def test1():
    s = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = s.buildTree(preorder, inorder)
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    assert root.right.left.val == 15
    assert root.right.right.val == 7


def test2():
    s = Solution()
    preorder = [3, 9, 20]
    inorder = [9, 3, 20]
    root = s.buildTree(preorder, inorder)
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
