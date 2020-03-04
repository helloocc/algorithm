#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def searchRange1(self, nums: list, target: int) -> list:
        """
        二分查找后往两边扩展找是否出现。
        """
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] < target:
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                res = [mid, mid]
                for i in range(low, mid)[::-1]:
                    if nums[i] == target:
                        res[0] = i
                    else:
                        break
                for i in range(mid, high+1):
                    if nums[i] == target:
                        res[1] = i
                    else:
                        break
                return res
        return [-1, -1]

    def searchRange2(self, nums: list, target: int) -> list:
        def search(n):
            low, high = 0, len(nums)
            while low < high:
                mid = (low + high) // 2
                if nums[mid] >= n:
                    high = mid
                else:
                    low = mid + 1
            return low
        low = search(target)
        return [low, search(target+1)-1] if target in nums[low:low+1] else [-1, -1]


@pytest.mark.parametrize(('nums', 'target', 'res'),
                         [([2, 2], 1, [-1, -1]),
                          ([2, 2], 2, [0, 1]),
                          ([2, 2, 2], 2, [0, 2]),
                          ([3, 4, 4], 3, [0, 0]),
                          ([3, 4, 4], 5, [-1, -1]),
                          ([1, 2, 3, 4], 2, [1, 1]),
                          ([1, 2, 3, 4, 5], 3, [2, 2]),
                          ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
                          ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
                          ])
def test1(nums, target, res):
    s = Solution()
    assert s.searchRange1(nums, target) == res
    assert s.searchRange2(nums, target) == res
