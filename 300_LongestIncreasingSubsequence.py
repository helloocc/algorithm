#!/usr/bin/env python
# -*- coding=utf8 -*-

from typing import List
import pytest


class Solution:
    """
    详细思路：https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-er-fen-cha-zhao-tan-xin-suan-fa-p/
    """

    def lengthOfLIS1(self, nums: List[int]) -> int:
        """
        DP:
        1. 定义状态：dp[i] 表示以 nums[i]结尾的「上升子序列」的长度
        2. 遍历nums[i]之前的数字，只要nums[i]大于它，则可以在它的基础上形成一个更长的子序列
        3. 状态转移：dp[i] = max(dp[i], dp[j] + 1) if nums[i] > nums[j]
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        """
        贪心+二分查找：维护tail数组
        tail[i] 表示长度固定为i+1的所有「上升子序列」的结尾元素中最小的那个，结果就是tail的长度。
        """
        if not nums:
            return 0
        tail = [nums[0]]
        for num in nums:
            # 大于tail的最后一个数，则可以形成更长的子序列
            if num > tail[-1]:
                tail.append(num)
            # 小于tail的最后一个数，则替换最近小于num的后面一个位置，二分查找更快
            elif num < tail[-1]:
                i, j = 0, len(tail) - 1
                while i < j:
                    mid = (i + j) // 2
                    if num > tail[mid]:
                        i = mid + 1
                    else:
                        # 不能-1，因为有可能就是j位置被替换
                        j = mid
                tail[i] = num

        return len(tail)


@pytest.mark.parametrize(("param", "ret"), [([1, 2, 4, 3], 3),
                                            ([10, 9, 2, 5, 3, 4], 3),
                                            ([4, 10, 4, 3, 8, 9], 3),
                                            ([18, 55, 66, 2, 3, 54], 3),
                                            ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6),
                                            ([10, 9, 2, 5, 3, 7, 101, 18], 4),
                                            ([0], 1),
                                            ([1, 2], 2),
                                            ([2, 2], 1),
                                            ([1, 2, 0], 2)])
def test1(param, ret):
    solution = Solution()
    assert solution.lengthOfLIS1(param) == ret
    assert solution.lengthOfLIS2(param) == ret
