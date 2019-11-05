#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def removeDuplicates1(self, nums: list) -> int:
        """
        思想：列表移除数据时列表长度会变，所以每次长度要减一。
        """
        i, lens = 0, len(nums)
        while i < lens-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
                lens -= 1
            else:
                i += 1
        return len(nums)

    def removeDuplicates2(self, nums: list) -> int:
        """
        优化：逆序移除时索引不会异常。
        """
        for i in range(len(nums))[::-1]:
            if i == 0:
                break
            if nums[i] == nums[i-1]:
                nums.pop(i)
        return len(nums)


@pytest.mark.parametrize(('param', 'res'), [([1, 1, 2], 2),
                                            ([1], 1),
                                            ([1, 1], 1),
                                            ([0, 0, 1, 1, 2, 2, 3, 3, 4], 5)])
def test1(param, res):
    s = Solution()
    assert s.removeDuplicates1(param) == res


@pytest.mark.parametrize(('param', 'res'), [([1, 1, 2], 2),
                                            ([1], 1),
                                            ([1, 1], 1),
                                            ([0, 0, 1, 1, 2, 2, 3, 3, 4], 5)])
def test2(param, res):
    s = Solution()
    assert s.removeDuplicates2(param) == res
