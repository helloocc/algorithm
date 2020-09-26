#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pathSum1(self, root: TreeNode, sum: int) -> int:
        """
        前缀和+记忆优化，参考560题解
        """
        target = sum
        # 补位0，单结点满足条件的场景
        memo = {0: 1}

        def dfs(node, cursum):
            if not node:
                return 0
            cursum += node.val
            # 计算当前结点
            count = memo.get(cursum-target, 0)
            memo[cursum] = memo.get(cursum, 0)+1
            # 计算子结点
            sub = dfs(node.left, cursum)+dfs(node.right, cursum)
            # 递归回溯时需要删除
            memo[cursum] -= 1
            return count+sub

        return dfs(root, 0)

    def pathSum2(self, root: TreeNode, sum: int) -> int:
        """
        https://leetcode-cn.com/problems/path-sum-iii/solution/437zhi-xu-yi-ci-di-gui-wu-xing-dai-ma-yong-lie-bia/
        """
        def dfs(node, sumlist):
            if not node:
                return 0
            # 计算路径上所有结点到当前结点的sum
            sumlist = [num + node.val for num in sumlist] + [node.val]
            return sumlist.count(sum)+dfs(node.left, sumlist)+dfs(node.right, sumlist)

        return dfs(root, [])


def test1():
    s = Solution()
    a, b, c = TreeNode(10), TreeNode(5), TreeNode(-3)
    a.left, a.right = b, c
    d, e, f = TreeNode(3), TreeNode(2), TreeNode(11)
    b.left, b.right, c.right = d, e, f
    g, h, i = TreeNode(3), TreeNode(-2), TreeNode(1)
    d.left, d.right, e.right = g, h, i
    assert s.pathSum1(a, 8) == 3
    assert s.pathSum2(a, 8) == 3


def test2():
    s = Solution()
    a = TreeNode(1)
    assert s.pathSum1(a, 0) == 0
    assert s.pathSum2(a, 0) == 0
