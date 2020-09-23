#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    def findUnsortedSubarray1(self, nums: List[int]) -> int:
        """
        原数组排序再比较，求出左右两边不满足要求的索引
        """
        new = sorted(nums)
        l, r = 0, len(nums) - 1
        while l < r and nums[l] == new[l]:
            l += 1
        while l < r and nums[r] == new[r]:
            r -= 1
        return r - l + 1 if r > l else 0

    def findUnsortedSubarray2(self, nums: List[int]) -> int:
        """
        1.从数组两端遍历找破坏升序顺序的索引，从而确定需要无序的连续子数组
        2.在无序子数组中找出最大值和最小值
        3.再次从两端遍历，找出最大值和最小值正确的索引，两者之差即为最短无序子数组
        """
        l, r = 0, len(nums) - 1
        while l < r and nums[l] <= nums[l + 1]:
            l += 1
        while l < r and nums[r] >= nums[r - 1]:
            r -= 1

        if l == r:
            return 0

        min_, max_ = min(nums[l:r + 1]), max(nums[l:r + 1])

        l, r = 0, len(nums) - 1
        while l < r and min_ >= nums[l]:
            l += 1
        while l < r and max_ <= nums[r]:
            r -= 1
        return r - l + 1


@pytest.mark.parametrize(('param', 'ret'), [
    ([2, 6, 4, 8, 10, 9, 15], 5),
    ([1, 1, 2], 0),
    ([3, 1, 4], 2),
    ([1, 3, 2, 2], 3),
    ([1, 3, 5, 4, 2], 4),
    ([3, 2, 1], 3)])
def test1(param, ret):
    solution = Solution()
    assert solution.findUnsortedSubarray1(param) == ret
    assert solution.findUnsortedSubarray2(param) == ret
