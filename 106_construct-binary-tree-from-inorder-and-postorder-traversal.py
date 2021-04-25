#!/usr/bin/env python
# -*- coding: utf8 -*-
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return
        root = TreeNode(postorder.pop())
        index = inorder.index(root.val)

        # 先右子树再左子树
        # 因为根节点是由后序遍历的tail确定，而后序的顺序是left->right->root
        # 所以下一次的tail应该是属于root的右子树
        root.right = self.buildTree(inorder[index+1:], postorder)
        root.left = self.buildTree(inorder[:index], postorder)
        return root


def print_tree(node: List[TreeNode]):
    res = []
    queue = [node]
    while queue:
        node = queue.pop(0)
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return res


s = Solution()
inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
res = [3, 9, 20, 15, 7]
print_tree(s.buildTree(inorder, postorder))


def test1():
    s = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    res = [3, 9, 20, 15, 7]
    assert res == print_tree(s.buildTree(inorder, postorder))


def test2():
    s = Solution()
    inorder = [-1]
    postorder = [-1]
    res = [-1]
    assert res == print_tree(s.buildTree(inorder, postorder))
