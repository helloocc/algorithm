#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        DP：dp[i][j]代表以matrix[i][j]为正方形右下角时，区域内最大square的边长
        """
        if not matrix:
            return 0
        m, n, max_lens = len(matrix), len(matrix[0]), 0
        # dp补位左边和上边
        dp = [[0 for _ in range(n + 1)]for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                # dp的索引要比matrix索引大1
                x, y = i + 1, j + 1
                if matrix[i][j] == '1':
                    dp[x][y] = min(dp[x][y - 1],
                                   dp[x - 1][y],
                                   dp[x - 1][y - 1]) + 1
                    max_lens = max(dp[x][y], max_lens)
        return max_lens * max_lens


@pytest.mark.parametrize(('param', 'ret'), [
    ([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]], 4),
    ([
        ["1", "0", "1"],
        ["1", "1", "1"],
        ["1", "0", "0"]], 1),
    ([
        ["1", "1"],
        ["1", "1"]], 4),
    ([
        ["0", "1"]], 1),
    ([], 0)])
def test1(param, ret):
    solution = Solution()
    assert solution.maximalSquare(param) == ret
