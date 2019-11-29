#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    """
    f(0) = nums[0]
    f(1) = max(num[0], num[1])
    f(k) = max(f(k-2) + nums[k], f(k-1))
    """

    def rob1(self, nums: list) -> int:
        """
        转换为DP.
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[-1]

    def rob2(self, nums: list) -> int:
        """
        只需返回最后的结果，无需通过dp记录中间状态。
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        pre, cur = 0, 0
        for i in range(len(nums)):
            pre, cur = cur, max(pre+nums[i], cur)
        return cur


@pytest.mark.parametrize(("param", "ret"), [([1, 2, 3, 1], 4),
                                            ([2, 3, 3], 5),
                                            ([1, 5, 3], 5),
                                            ([], 0),
                                            ([0], 0),
                                            ([1, 2], 2),
                                            ([2, 1, 1, 2], 4),
                                            ([1, 5, 6, 3], 8),
                                            ([2, 7, 9, 3, 1], 12)])
def test1(param, ret):
    solution = Solution()
    assert solution.rob1(param) == ret
    assert solution.rob2(param) == ret
