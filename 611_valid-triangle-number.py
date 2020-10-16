#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    """
    双指针，类似题解015，3sum
    """

    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        count = 0
        nums.sort()
        for i in range(2, len(nums))[::-1]:
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    # l..r-1 都满足 nums[x] + nums[r] > nums[i]
                    # l..r-1 共有 (r-1)-l+1 种可能
                    count += (r - l)
                    r -= 1
                else:
                    l += 1
        return count


@pytest.mark.parametrize(('param', 'ret'), [([2, 2, 3, 4], 3),
                                            ([1, 2, 3, 4, 5, 6], 7),
                                            ([24, 3, 82, 22, 35, 84, 19], 10),
                                            ([0, 1, 0], 0),
                                            ([2, 3, 2], 1),
                                            ([2, 2, 4], 0)])
def test1(param, ret):
    solution = Solution()
    assert solution.triangleNumber(param) == ret
