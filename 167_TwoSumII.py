#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        """
        已经有序的数组，使用首尾指针，相加大于target时尾指针前移，小于时首指针后移。
        """
        i, j = 0, len(numbers)-1
        while i < j:
            total = numbers[i]+numbers[j]
            if total == target:
                return [i+1, j+1]
            elif total > target:
                j -= 1
            elif total < target:
                i += 1


@pytest.mark.parametrize(('nums', 'target', 'ret'), [([2, 7, 11, 15], 9, [1, 2]),
                                                     ([2, 4], 6, [1, 2]),
                                                     ([3, 3], 6, [1, 2]),
                                                     ([1, 2, 3], 4, [1, 3])])
def test1(nums, target, ret):
    solution = Solution()
    a = list(nums)
    assert solution.twoSum(a, target) == ret
