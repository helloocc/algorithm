#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:

    def trailingZeroes1(self, n: int) -> int:
        """
        https://leetcode.com/problems/factorial-trailing-zeroes/discuss/196311/topic

        2和5相乘为0，本质求2和5的个数，最终转换为5的个数，有几对2*5结尾就有几个0。

        递归公式：f(n) = n/5 + f(n/5)
        """
        if (n < 5):
            return 0
        if (n < 10):
            return 1
        return n // 5 + self.trailingZeroes1(n // 5)

    def trailingZeroes2(self, n: int) -> int:
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res


@pytest.mark.parametrize(("param", "ret"), [(3, 0),
                                            (5, 1),
                                            (10, 2),
                                            (30, 7)])
def test1(param, ret):
    solution = Solution()
    assert solution.trailingZeroes1(param) is ret
    assert solution.trailingZeroes2(param) is ret
