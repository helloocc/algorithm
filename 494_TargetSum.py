#!/usr/bin/env python
#-*- coding=utf8 -*-

from typing import List
import pytest


class Solution:
    def findTargetSumWays1(self, nums: List[int], S: int) -> int:
        """
        简单的dfs会超时，需要进行优化。

        以[1,1,1] 为例:
                  0
             /           \
            -1            1
           /   \        /   \
         -2     0      0     2    # 当所在层数相同且sum相同时，则后面dfs的结果也是相同的，不用重复计算
          /\    /\     /\    /\
        -3 -1 -1  1  -1  1  1  3

        将当前层数及sum值存到dict，后面计算时遇到相同key直接取vaule即可（这里需要理解，dfs是自底向上返回值，所以从dict中取到的value，是当前key从底往上的返回值，即所有结果）
        """
        memo = dict()

        def dfs(nums, index, total, target):
            if index == len(nums):
                return 1 if total == target else 0
            if (index, total) in memo.keys():
                return memo[(index, total)]
            else:
                memo[(index, total)] = dfs(nums, index+1, total+nums[index],target) + dfs(nums, index+1, total-nums[index], target)
                return memo[(index, total)]

        return dfs(nums, 0, 0, S)


    def findTargetSumWays2(self, nums: List[int], S: int) -> int:
        """
        DP：假设P为正数集合，N为负数集合
        推导：
                          sum(P) - sum(N) = target
        sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
                              2  * sum(P) = target + sum(nums)

        参考题解416，本题是在数组中找到一些数和为 (target+sum)/2，所以target+sum必须为偶数
        """
        total = sum(nums)
        if abs(S) > abs(total) or (total+S) % 2 == 1:
            return 0
        target, lens = (total+S)//2, len(nums)

        # target+1是因为要计算和为0的场景
        dp = [[0 for y in range(target+1)] for x in range(lens)]

        # 计算i=0 的场景，当nums[0]为0时，+0，-0都成立，故有两种
        dp[0][0] = 1 if nums[0] else 2
        if 0 < nums[0] <= target:
            dp[0][nums[0]] = 1

        for i in range(1, lens):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
        return dp[-1][-1]


@pytest.mark.parametrize(("nums", "target", "res"),
                         [([1, 1, 1, 1, 1], 3, 5),
                          ([1, 1], 2, 1),
                          ([1, 1], 0, 2),
                          ([1, 2, 3], 0, 2),
                          ([1], 2, 0),
                          ([1, 2], -4, 0),
                          ([0, 0, 0, 0, 0, 0, 0, 0, 1], 1, 256),
                          ([1], -1, 1)])
def test1(nums, target, res):
    solution = Solution()
    assert solution.findTargetSumWays1(nums, target) == res
    assert solution.findTargetSumWays2(nums, target) == res
