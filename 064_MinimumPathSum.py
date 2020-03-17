#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def minPathSum1(self, grid: list) -> int:
        """
        DP：新建二维数组记录最短路径
        """
        x, y = len(grid), len(grid[0])
        dp = [[0 for _ in range(y)] for _ in range(x)]

        for i in range(x):
            for j in range(y):
                if i == 0:
                    dp[0][j] = dp[0][j-1]+grid[0][j]
                elif j == 0:
                    dp[i][0] = dp[i-1][0]+grid[i][0]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j])+grid[i][j]
        return dp[-1][-1]

    def minPathSum2(self, grid: list) -> int:
        """
        DP：修改grid本身记录当前的最短路径
        """
        x, y = len(grid), len(grid[0])

        for i in range(1, x):
            grid[i][0] = grid[i-1][0]+grid[i][0]

        for j in range(1, y):
            grid[0][j] = grid[0][j-1]+grid[0][j]

        for i in range(1, x):
            for j in range(1, y):
                grid[i][j] = min(grid[i][j-1], grid[i-1][j])+grid[i][j]
        return grid[-1][-1]


@pytest.mark.parametrize(('param,ret'), [([[1, 3, 1],
                                           [1, 5, 1],
                                           [4, 2, 1]], 7),

                                         ([[1, 1, 2],
                                           [1, 2, 2],
                                           [4, 1, 1]], 6),

                                         ([[1]], 1),

                                         ([[1, 2, 1],
                                           [1, 1, 1]], 4)])
def test(param, ret):
    s = Solution()
    assert s.minPathSum1(param) == ret
    assert s.minPathSum2(param) == ret
