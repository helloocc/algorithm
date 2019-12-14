#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def maxProfit(self, prices: list) -> int:
        """
        峰谷模式：每次都要找到subtransaction的买入点和卖出点，而利润等于递增子序列之和。
        A-> B + B-> C + C-> D = A-> D
        
        图解：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/solution/
        """
        total = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                total += (prices[i+1]-prices[i])
        return total


@pytest.mark.parametrize(("param", "ret"), [([7, 1, 5, 3, 6, 4], 7),
                                            ([1, 2, 3, 4, 5], 4),
                                            ([7, 6, 5, 4, 3], 0)])
def test1(param, ret):
    solution = Solution()
    assert solution.maxProfit(param) == ret
