#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest
from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        1. 从左往右遍历，得到该数左边所有数的乘积
        2. 从右往左遍历，得到该数右边所有数的乘积
        3. 左边乘积*右边乘积即为结果
        """
        n = len(nums)
        left, right = [1] * n, [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for j in range(n - 1)[::-1]:
            right[j] = right[j + 1] * nums[j + 1]

        return [left[i] * right[i] for i in range(n)]


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))


@pytest.mark.parametrize(('param', 'ret'), [([1, 2, 3, 4], [24, 12, 8, 6]),
                                            ([2, 2, 3], [6, 6, 4]),
                                            ([1, 1, 0], [0, 0, 1]),
                                            ([1, 2], [2, 1]),
                                            ([1, 1], [1, 1])])
def test1(param, ret):
    solution = Solution()
    assert solution.productExceptSelf(param) == ret
