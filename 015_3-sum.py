#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def threeSum(self, nums: list) -> list:
        """
        思路：遍历+双指针
        首先进行排序，然后开始遍历nums，再设定左右指针，三数之和进行判定。
        如果小于0，则移动左指针，大于0则移动右指针。等于0时左右指针同时移动，需要判定相等的情况。

        需要考虑各种边界场景。
        """
        ret = []
        nums.sort()
        for i in range(len(nums)-2):
            # 排序后若最小数大于0，则无需继续判断
            if nums[i] > 0:
                break
            # 该场景[0, 0, 0, 0] 需要判断i>0
            if i and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                target = nums[i]+nums[l]+nums[r]
                if target == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    # [-2, 0, 0, 2, 2] 该场景移动l,r需要继续判断
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
        return ret


@pytest.mark.parametrize('nums,ret', [
    ([-1, 0, 1, 2,  -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([1, 3, 0, -1, -2], [[-2, -1, 3], [-1, 0, 1]]),
    ([0, 0, 0, 0], [[0, 0, 0]]),
    ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
    ([2, 3, 2, 2], []),
    ([0, 0, 1], []),
    ([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0],
     [[-5, 1, 4], [-4, 0, 4], [-4, 1, 3], [-2, -2, 4], [-2, 1, 1], [0, 0, 0]]),
    ([0, 0, 0], [[0, 0, 0]])])
def test1(nums, ret):
    s = Solution()
    assert s.threeSum(nums) == ret
