#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
import math
import pytest


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        """
        二分查找
        """
        def satisfy(hour, speed):
            used = sum(math.ceil(x / speed) for x in piles)
            return used <= hour

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if satisfy(H, mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


@pytest.mark.parametrize(('piles', 'hour', 'speed'), [
    ([3, 6, 7, 11], 8, 4),
    ([30, 11, 23, 4, 20], 5, 30),
    ([30, 11, 23, 4, 20], 6, 23)])
def test1(piles, hour, speed):
    solution = Solution()
    assert solution.minEatingSpeed(piles, hour) == speed
