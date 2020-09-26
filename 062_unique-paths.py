#!/usr/bin/env python
# -*- coding=utf8 -*-

import pytest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        典型DP
        递推公式: dp[i][j]=dp[i-1][j]+dp[i][j-1]
        """
        dp = [[1 for y in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]


@pytest.mark.parametrize(('m', 'n', 'res'), [(3, 2, 3),
                                             (7, 3, 28),
                                             (3, 3, 6),
                                             (2, 2, 2)])
def test1(m, n, res):
    s = Solution()
    assert s.uniquePaths(m, n) == res
