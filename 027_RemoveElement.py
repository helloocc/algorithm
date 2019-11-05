#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        """
        思想：逆序移除时索引不会异常。
       """
        for i in range(len(nums))[::-1]:
            if nums[i] == val:
                nums.pop(i)
        return len(nums)


@pytest.mark.parametrize(('param', 'val', 'res'), [([3, 2, 2, 3], 3, 2),
                                                   ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5)])
def test1(param, val, res):
    s = Solution()
    assert s.removeElement(param, val) == res
