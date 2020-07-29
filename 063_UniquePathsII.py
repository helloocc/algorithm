#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    def uniquePathsWithObstacles1(self, obstacleGrid: List[List[int]]) -> int:
        """
        典型DP
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0 if obstacleGrid[0][0] else 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    if i:
                        dp[i][j] += dp[i-1][j]
                    if j:
                        dp[i][j] += dp[i][j-1]
        return dp[-1][-1]

    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        """
        二维数组压缩成一维数组
            dp[j]    = dp[j]     + dp[j - 1]
        new dp[j]    = old dp[j] + dp[j-1]
        current cell = top cell  + left cell
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0]*n
        dp[0] = 0 if obstacleGrid[0][0] else 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                else:
                    if j and obstacleGrid[i][j-1] == 0:
                        dp[j] += dp[j-1]
        return dp[n-1]


@pytest.mark.parametrize(('param,ret'), [
    ([[0, 0, 0],
      [0, 1, 0],
      [0, 0, 0]], 2),
    ([[0, 0],
      [0, 0]], 2),
    ([[1, 0],
      [0, 0]], 0),
    ([[0, 1, 0],
      [0, 0, 0]], 1)])
def test(param, ret):
    solution = Solution()
    assert solution.uniquePathsWithObstacles1(param) == ret
    assert solution.uniquePathsWithObstacles2(param) == ret
