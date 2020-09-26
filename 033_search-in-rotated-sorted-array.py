#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def search(self, nums: list, target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid

            # 这里要加上=，因为当low+high为奇数时，mid更接近low的位置。
            elif nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1


@pytest.mark.parametrize(('nums', 'target', 'res'), [([5, 1, 2, 3, 4], 2, 2),
                                                     ([3, 4, 1, 2], 4, 1),
                                                     ([4, 5, 6, 7, 0, 1, 2], 0, 4),
                                                     ([4, 5, 6, 7, 0, 1, 2], 3, -1),
                                                     ([4, 5, 6, 7, 0, 1, 2, 3], 3, 7),
                                                     ([5, 6, 7, 0, 1, 2, 3, 4], 7, 2),
                                                     ([5, 2], 1, -1),
                                                     ([5, 2], 2, 1),
                                                     ([5, 2], 5, 0),
                                                     ])
def test1(nums, target, res):
    s = Solution()
    assert s.search(nums, target) == res
