#!/usr/bin/env python
# -*- coding=utf8 -*-


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    分析：爷爷偷的钱 + 4个孙子偷的钱 VS 两个儿子偷的钱，哪个组合钱多，就当做当前节点能偷的最大钱数。
    """

    def rob1(self, root: TreeNode) -> int:
        """
        DFS记忆优化，无需重复计算
        """
        memo = dict()

        def dfs(node):
            if not node:
                return 0
            if node in memo.keys():
                return memo[node]
            money = node.val
            if node.left:
                money += dfs(node.left.left)+dfs(node.left.right)
            if node.right:
                money += dfs(node.right.left)+dfs(node.right.right)
            res = max(money, dfs(node.left)+dfs(node.right))
            memo[node] = res
            return res

        return dfs(root)

    def rob2(self, root: TreeNode) -> int:
        """
        DP树形版本
        1. 定义状态: dp[node][j] 表示node结点能够获得的最大值。
           a) j = 0 表示 node 结点不偷取
           b) j = 1 表示 node 结点偷取

        2. 状态转移方程: 根据当前结点偷或者不偷，就决定了需要从哪些子结点里的对应的状态转移过来。
           a) 如果当前结点偷，左右子结点均不能偷。
           b) 如果当前结点不偷，左右子结点偷或者不偷都行，选最大者
        """

        def dfs(node):
            if not node:
                return 0, 0
            left, right = dfs(node.left), dfs(node.right)

            # 当前结点不偷，取子结点的最大值
            rob_not = max(left)+max(right)
            # 当前结点偷，子结点都不能偷
            rob_now = node.val+left[0]+right[0]

            return rob_not, rob_now

        return max(dfs(root))


def test1():
    a, b, c, d, e = TreeNode(3), TreeNode(
        2), TreeNode(3), TreeNode(3), TreeNode(1)
    a.left, a.right = b, c
    b.right = d
    c.right = e
    s = Solution()
    assert s.rob1(a) == 7
    assert s.rob2(a) == 7


def test2():
    a, b, c, d, e, f = TreeNode(3), TreeNode(
        4), TreeNode(5), TreeNode(1), TreeNode(3), TreeNode(1)
    a.left, a.right = b, c
    b.left, b.right = d, e
    c.right = f
    s = Solution()
    assert s.rob1(a) == 9
    assert s.rob2(a) == 9


def test3():
    a, b, c, d = TreeNode(4), TreeNode(1), TreeNode(2),  TreeNode(3)
    a.left, b.left, c.left = b, c, d
    s = Solution()
    assert s.rob1(a) == 7
    assert s.rob2(a) == 7
