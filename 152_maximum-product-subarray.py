#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest
from typing import List


class Solution:

    def maxProduct1(self, nums: List[int]) -> int:
        """
        dp[i]记录num[i]的最优解。
        由于存在负数，会导致最大的变最小的，最小的变最大的。
        所以维护两个数组，分别记录最大值和最小值。
        """
        dp_max = [nums[0]] * len(nums)
        dp_min = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            dp_max[i] = max(dp_max[i - 1] * nums[i],
                            dp_min[i - 1] * nums[i], nums[i])
            dp_min[i] = min(dp_max[i - 1] * nums[i],
                            dp_min[i - 1] * nums[i], nums[i])
        return max(dp_max)

    def maxProduct2(self, nums: List[int]) -> int:
        """
        Kadane算法，类似053题解。
        无需记录所有的dp，只需记录前一个最优解即可。
        """
        max_now = min_now = max_prodcut = nums[0]
        for i in range(1, len(nums)):
            tmp = max_now
            max_now = max(max_now * nums[i], nums[i], min_now * nums[i])
            # 由于max_now已经重新计算，所以需要一个临时变量记录之前的max_now
            min_now = min(tmp * nums[i], nums[i], min_now * nums[i])
            max_prodcut = max(max_now, max_prodcut)
        return max_prodcut


@pytest.mark.parametrize(('param', 'ret'), [([2, 3, -2, 4], 6),
                                            ([-2, 0, -1], 0),
                                            ([-2], -2),
                                            ([-2, 1], 1),
                                            ([-3, -1, -1], 3),
                                            ([3, -1, 4], 4),
                                            ([2, -5, -2, -4, 3], 24),
                                            ([3, 1, -4, 2], 3)])
def test1(param, ret):
    solution = Solution()
    assert solution.maxProduct1(param) == ret
    assert solution.maxProduct2(param) == ret
