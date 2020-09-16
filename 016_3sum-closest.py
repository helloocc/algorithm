#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        类似题解015，遍历+双指针，本题需要多计算一个gap值而已。
        """
        nums.sort()
        min_gap, res = float('inf'), 0
        for i in range(len(nums) - 1):
            l, r = i + 1, len(nums) - 1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == target:
                    return summ
                elif summ < target:
                    l += 1
                elif summ > target:
                    r -= 1

                gap = abs(summ - target)
                if gap < min_gap:
                    min_gap = gap
                    res = summ
        return res


@pytest.mark.parametrize(('nums', 'target', 'ret'), [
    ([-1, 2, 1, -4], 1, 2),
    ([3, 1, 5, 2], 10, 10),
    ([-1, 0, 1, 2], 1, 1),
    ([-5, -1, 0, 2, 3], -7, -6),
    ([1, 2, 3], 4, 6)])
def test1(nums, target, ret):
    solution = Solution()
    assert solution.threeSumClosest(nums, target) == ret
