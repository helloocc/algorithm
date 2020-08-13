#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        """
        DP：
        1.定义状态：每天有两种状态，持有或不持有，求最后一天不持有的利润
        2.状态转移：
            a. 持有状态分2种
                1. 前一天就是持有状态，当天不操作
                2. 前两天是不持有状态，冷却一天，当天买入
            b. 不持有状态分2种
                1. 前一天也是不持有状态，当天不操作
                2. 前一天是持有状态，当天卖出
        """
        if not prices:
            return 0

        hold = [0] * len(prices)
        unhold = [0] * len(prices)
        hold[0] = -prices[0]

        for i in range(1, len(prices)):
            # i=1时，hold[1]=max(-prices[0],-prices[1])
            hold[i] = max(hold[i - 1], unhold[i - 2] - prices[i])
            unhold[i] = max(unhold[i - 1], hold[i - 1] + prices[i])
        return unhold[-1]

    def maxProfit2(self, prices: List[int]) -> int:
        """
        DP: 定义三个状态：buy,sell,rest
        """
        if not prices:
            return 0

        buy = [0] * len(prices)
        sell = [0] * len(prices)
        rest = [0] * len(prices)
        buy[0] = -prices[0]

        for i in range(1, len(prices)):
            buy[i] = max(buy[i - 1], rest[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            rest[i] = sell[i - 1]
        return max(sell[-1], rest[-1])


@pytest.mark.parametrize(("param", "ret"), [([1, 2, 3, 0, 2], 3),
                                            ([1, 2, 4], 3),
                                            ([1, 3], 2)])
def test1(param, ret):
    solution = Solution()
    assert solution.maxProfit1(param) == ret
    assert solution.maxProfit2(param) == ret
