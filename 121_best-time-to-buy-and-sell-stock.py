#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def maxProfit(self, prices: list) -> int:
        """
        这个问题可以转换为找到最大卖出价格和找到最小买入价格的问题。定义两个变量，表示买入价格和利润:

        1.如果当前价格比记录的买入价格更低，则设定当前为买入价格；
        2.当前价格和记录的买入价格相减，如果大于当前利润，则更新最大利润。

        python无穷大/无穷小：float('inf'),float(-inf')
        """
        max_pro, buy_price = 0, float('inf')
        for price in prices:
            buy_price = min(buy_price, price)
            max_pro = max(max_pro, price-buy_price)
        return max_pro


@pytest.mark.parametrize(("param", "ret"), [([7, 1, 5, 3, 6, 4], 5),
                                            ([2, 1, 3], 2),
                                            ([1, 1], 0),
                                            ([], 0),
                                            ([7, 6, 4, 3, 1], 0)])
def test1(param, ret):
    s = Solution()
    assert s.maxProfit(param) == ret
