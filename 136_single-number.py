#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def singleNumber(self, nums: list) -> int:
        """
        异或：^异或标识符，x^x=0,x^0=x
        """
        ret = 0
        for x in nums:
            ret ^= x
        return ret


@pytest.mark.parametrize(("param", "ret"), [([4, 1, 2, 1, 2], 4),
                                            ([2, 2, 1], 1)])
def test1(param, ret):
    s = Solution()
    assert s.singleNumber(param) == ret
