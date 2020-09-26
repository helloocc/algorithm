#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        """
        在原列表中查找，如果找到补码，返回从i+1开始查找的索引。
        """
        for i, val in enumerate(nums):
            other = target-val
            if other in nums[i+1:]:
                return [i, nums.index(other, i+1)]

    def twoSum1(self, nums: list, target: int) -> list:
        """
        空间换时间：新建dict，存于dict中方便查找（Hash查找速度快）。
        """
        dic = dict()
        for i, val in enumerate(nums):
            other = target-val
            if other in dic:
                return [dic.get(other), i]
            dic[val] = i


@pytest.mark.parametrize(('nums', 'target', 'ret'), [([2, 7, 11, 15], 9, [0, 1]),
                                                     ([2, 4], 6, [0, 1]),
                                                     ([3, 2, 4], 6, [1, 2]),
                                                     ([3, 3], 6, [0, 1]),
                                                     ([1, 2, 3], 4, [0, 2])])
def test1(nums, target, ret):
    solution = Solution()
    a = list(nums)
    assert solution.twoSum(a, target) == ret
    b = list(nums)
    assert solution.twoSum1(b, target) == ret
