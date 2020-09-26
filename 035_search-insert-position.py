#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def searchInsert1(self, nums: list, target: int) -> int:
        for i, x in enumerate(nums):
            if x >= target:
                return i
        return i+1

    def searchInsert2(self, nums: list, target: int) -> int:
        """
        二分查找效率更高，注意在头部插入的特殊场景。
        """
        if target <= nums[0]:
            return 0
        l, h = 0, len(nums)-1
        while l <= h:
            mid = (l+h)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                h = mid-1
        return l


@pytest.mark.parametrize(('param', 'val', 'res'), [([1, 3, 5, 6], 5, 2),
                                                   ([1, 3, 5, 6], 7, 4),
                                                   ([1, 3, 5, 6], 0, 0),
                                                   ([1, 3, 5], 1, 0),
                                                   ([1, 3, 5], 3, 1),
                                                   ([1, 3, 5, 6], 3, 1),
                                                   ([1, 3, 5, 6], 5, 2),
                                                   ([1, 3, 5, 6], 6, 3),
                                                   ([1, 2, 3, 4, 5, 6], 2, 1),
                                                   ([1, 3,  6], 6, 2),
                                                   ([0, 2], 1, 1),
                                                   ([0, 2], 3, 2),
                                                   ([1, 3, 5, 6], 2, 1)])
def test1(param, val, res):
    s = Solution()
    assert s.searchInsert1(param, val) == res
    assert s.searchInsert2(param, val) == res
