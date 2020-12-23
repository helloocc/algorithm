#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[-1], dp[-2])


@ pytest.mark.parametrize(('param', 'ret'), [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ([1, 2, 1], 2),
    ([1, 2, 1, 2], 2)])
def test1(param, ret):
    solution = Solution()
    assert solution.minCostClimbingStairs(param) == ret
