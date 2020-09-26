#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def findDisappearedNumbers1(self, nums: list) -> list:
        """
        不做set操作会超时，但此解使用了多余的空间。
        """
        f_num = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in f_num]

    def findDisappearedNumbers2(self, nums: list) -> list:
        """
        解释：https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/344583/Python%3A-O(1)-space-solution
        """
        for _, x in enumerate(nums):
            index = abs(x)-1
            nums[index] = -abs(nums[index])
        return [i+1 for i, x in enumerate(nums) if x > 0]


@pytest.mark.parametrize(('nums', 'ret'), [([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
                                           ([1, 1], [2]),
                                           ([1, 3, 4, 3], [2])])
def test1(nums,  ret):
    solution = Solution()
    a = list(nums)
    assert solution.findDisappearedNumbers1(a) == ret
    b = list(nums)
    assert solution.findDisappearedNumbers2(b) == ret
