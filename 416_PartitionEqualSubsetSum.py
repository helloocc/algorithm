#!/usr/bin/env python
#-*- coding=utf8 -*-

from typing import List
import pytest


class Solution:
    """
    等价转换：是否可以从数组中挑出一些正整数，使得这些数的和等于整个数组元素和的一半。因此，如果满足条件，则数组总和一定是偶数
    """

    def canPartition1(self, nums: List[int]) -> bool:
        """
        DFS：
        1. 对于nums中的每一个元素，要么放到子集1中，要么放到子集2中，这两种操作互补且等价
        2. 当任意一个子集和等于sum(nums)/2时，即成功找到一个解
        3. 当任意一个子集和大于sum(nums)/2时，在此种分支下不可能找到一个可行解，剪枝
        """
        def dfs(nums,target1, target2):
            if target1 == 0 or target2 == 0:
                return True
            if target1 < 0 or target2 < 0:
                return False
            return dfs(nums[1:], target1-nums[0], target2) or dfs(nums[1:], target1, target2-nums[0])

        nums.sort(reverse=True)
        total = sum(nums)
        return False if total % 2 else dfs(nums, total/2, total/2)


    def canPartition2(self, nums: List[int]) -> bool:
        """
        DP：类似0-1背包问题
        详解：https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/0-1-bei-bao-wen-ti-xiang-jie-zhen-dui-ben-ti-de-yo/

        1. 状态定义：dp[i][j]表示从数组的[0, i]区间内挑选一些正整数，使它们的和恰好等于j
        2. 状态转移方程：
            a. 不选择nums[i]：在[0, i-1]区间内已经有一部分元素，使得它们的和为j，那么dp[i][j] = true
            b. 选择nums[i]：在[0,i-1]区间内找到一部分元素，使得它们的和为j-nums[i]。

            dp[i][j] = dp[i-1][j] or dp[i-1][j-num[i]]
        """
        total = sum(nums)
        if total % 2 == 1:
            return False

        target, lens = total//2, len(nums)

        # target+1是因为要计算和为0的场景
        dp = [[False for j in range(target+1)] for i in range(lens)]

        # 计算i=0 的场景
        dp[0][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True

        for i in range(1,lens):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[-1][-1]


@pytest.mark.parametrize(("nums",  "res"),
                         [([1, 5, 11, 5], True),
                          ([1, 2, 3], True),
                          ([1, 2, 5], False),
                          ([1, 2, 3, 4, 5, 6, 7], True),
                          ([1, 1, 1, 1], True),
                          ([1, 1, 1], False),
                          ([1, 1], True),
                          ([1, 2, 3, 5], False)])
def test1(nums,  res):
    solution = Solution()
    assert solution.canPartition1(nums) == res
    assert solution.canPartition2(nums) == res
