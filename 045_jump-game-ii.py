#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    def jump1(self, nums: List[int]) -> int:
        """
        DP：dp[i]代表当前索引需要的最小步数

        1. 当前索引i位置的最小步数，取两者最小值，min(dp[i],dp(i-1)+1)
        2. [i+1,i+num]范围内的所有位置都可以由i位置一步到达,
           所以 dp[i+1]~dp[i+j] = min(dp[x],dp[i]+1)
        """
        dp = [float('inf')] * len(nums)
        dp[0] = 0

        for i in range(1, len(nums)):
            dp[i] = min(dp[i - 1] + 1, dp[i])
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]

    def jump2(self, nums: List[int]) -> int:
        """
        DP: 更容易理解的方法

        对于当前位置i，如果前面任意位置j的值可以到达，
        则dp[i]=min(dp[i],dp[j])+1)
        """
        dp = [float('inf')] * len(nums)
        dp[0] = 0

        for i in range(1, len(nums)):
            for j in range(i+1):
                if j+nums[j] >= i:
                    dp[i] = min(dp[i], dp[j]+1)
        return dp[-1]

    def jump3(self, nums: List[int]) -> int:
        """贪心

        https://leetcode-cn.com/problems/jump-game-ii/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-10/
        """
        end = farthest = count = 0

        # 不用算最后一个,所以是range(len-1)
        for i in range(len(nums)-1):
            # 下一跳的最大值
            farthest = max(farthest, i+nums[i])

            # 当前达到目标下一跳的位置
            if i == end:
                # 步数+1，更新边界
                count += 1
                end = farthest
        return count


@pytest.mark.parametrize(("param", "ret"), [([2, 3, 1, 1, 4], 2),
                                            ([1, 1, 1], 2),
                                            ([2], 0),
                                            ([0], 0),
                                            ([1, 2, 3], 2),
                                            ([2, 3, 0, 1, 4], 2)])
def test1(param, ret):
    s = Solution()
    assert s.jump1(param) == ret
    assert s.jump2(param) == ret
    assert s.jump3(param) == ret
