#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest


class Solution:
    """
    DP：类似爬楼梯的DP.
    注意：'10'有一种解法，而'100'没有解法
    """

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1

        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]


@pytest.mark.parametrize(('param', 'ret'), [('12', 2),
                                            ('226', 3),
                                            ('0', 0),
                                            ('00', 0),
                                            ('000', 0),
                                            ('01', 0),
                                            ('10', 1),
                                            ('100', 0),
                                            ('27', 1)])
def test1(param, ret):
    solution = Solution()
    assert solution.numDecodings(param) == ret
