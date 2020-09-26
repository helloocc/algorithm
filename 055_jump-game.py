#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:

    def canJump1(self, nums: list) -> bool:
        """
        贪心法：在遍历数组的过程中，更新每个点能跳到最远的范围，如果最后范围大于等于终点，就是可以跳到。
        """
        reach = 0
        for i, x in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i+x)
        return reach >= len(nums)-1

    def canJump2(self, nums: list) -> bool:
        """
        从后往前，如果可以到达，最后的goal是0.
        """
        goal = len(nums)-1
        for i in range(len(nums))[::-1]:
            if i+nums[i] >= goal:
                goal = i
        return not goal


@pytest.mark.parametrize(("param", "ret"), [([2, 3, 1, 1, 4], True),
                                            ([0, 2, 3], False),
                                            ([1, 1, 1], True),
                                            ([1, 2, 3], True),
                                            ([3, 2, 1, 0, 4], False)])
def test1(param, ret):
    s = Solution()
    assert s.canJump1(param) == ret
    assert s.canJump2(param) == ret
