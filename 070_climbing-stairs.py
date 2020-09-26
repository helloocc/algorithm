#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def climbStairs1(self, n: int) -> int:
        """
        DP：记录每个子问题的解法，避免重复计算.
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0]*(n+1)
        dp[0], dp[1], dp[2] = 0, 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

    def climbStairs2(self, n: int) -> int:
        """
        Fibonacci: 无需记录所有数值的解法，只需返回最终n的解法。
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a+b
        return b


@pytest.mark.parametrize(('param,ret'), ([1, 1], [2, 2], [3, 3], [4, 5]))
def test(param, ret):
    s = Solution()
    assert s.climbStairs1(param) == ret
    assert s.climbStairs2(param) == ret
