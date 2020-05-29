#!/usr/bin/env python
#-*- coding=utf8 -*-
import pytest


class Solution:
    """
    卡塔兰数：https://zh.wikipedia.org/wiki/%E5%8D%A1%E5%A1%94%E5%85%B0%E6%95%B0
    Cn = (2n)!/((n+1)!*n!)

    DP:
    dp[0] = 1  (空树也算一种二叉搜索树)

    dp[1] = 1  (可以看做是其左子树个数乘以右子树的个数，左右子树都是空树，所以1乘1还是1)

    dp[2] = dp[0] * dp[1]  (1为根的情况，则左子树一定不存在，右子树可以有一个数字)
          + dp[1] * dp[0]  (2为根的情况，则左子树可以有一个数字，右子树一定不存在)

    dp[3] = dp[0] * dp[2]  (1为根的情况，则左子树一定不存在，右子树可以有两个数字)
          + dp[1] * dp[1]  (2为根的情况，则左右子树都可以各有一个数字)
          + dp[2] * dp[0]  (3为根的情况，则左子树可以有两个数字，右子树一定不存在)

    G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0)
    """

    def numTrees1(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]

    def numTrees2(self, n: int) -> int:
        """
        将每个数字视为根，然后left part*right part
        """
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[n]

@pytest.mark.parametrize(('nums', 'ret'), [(1, 1),
                                           (2, 2),
                                           (3, 5)])
def test1(nums, ret):
    solution = Solution()
    assert solution.numTrees1(nums) == ret
    assert solution.numTrees2(nums) == ret
