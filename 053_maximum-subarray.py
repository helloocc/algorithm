#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def maxSubArray1(self, nums: list) -> int:
        """
        Kadane算法：https://zh.wikipedia.org/wiki/%E6%9C%80%E5%A4%A7%E5%AD%90%E6%95%B0%E5%88%97%E9%97%AE%E9%A2%98

        每个nums[i]存储的都是子问题的最优解。
        """
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1]+nums[i], nums[i])
        return max(nums)

    def maxSubArray2(self, nums: list) -> int:
        """
        动态规划
        """
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)


@pytest.mark.parametrize(("param", "ret"), [([-2, 1, -3, 4, -1, 2, 1, -5, 5], 6),
                                            ([-1, -2, -3, -4], -1),
                                            ([2, 2, 1, -1], 5)])
def test1(param, ret):
    s = Solution()
    copy1 = list(param)
    assert s.maxSubArray1(copy1) == ret
    copy2 = list(param)
    assert s.maxSubArray2(copy2) == ret
