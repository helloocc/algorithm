#!/usr/bin/env python
# -*- coding=utf8 -*-


from typing import List
import pytest


class Solution:
    """
    1.二进制奇数比前一位偶数多一个'1'
    2.二进制偶数中的'1'一定和该偶数除2的数中的'1'一样，因为末位是0，除2相当于把末位的0抹掉
    """

    def countBits1(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for x in range(num + 1):
            if x % 2:
                dp[x] = dp[x - 1] + 1
            else:
                dp[x] = dp[x >> 1]
        return dp

    def countBits2(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for x in range(num + 1):
            dp[x] = dp[x >> 1] + (x & 1)
        return dp


@pytest.mark.parametrize(("param", "ret"), [(2, [0, 1, 1]),
                                            (5, [0, 1, 1, 2, 1, 2]),
                                            (1, [0, 1])])
def test1(param, ret):
    solution = Solution()
    assert solution.countBits1(param) == ret
    assert solution.countBits2(param) == ret
