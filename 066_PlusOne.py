#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def plusOne1(self, digits: list) -> list:
        """
        使用新数组记录
        """
        carry, res = 1, []
        for x in digits[::-1]:
            if carry == 0:
                res.append(x)
            else:
                carry, x = divmod(x+carry, 10)
                res.append(x)
        if carry:
            res.append(carry)
        return res[::-1]

    def plusOne2(self, digits: list) -> list:
        """
        修改原数组
        """
        carry, lens = 1, len(digits)-1
        for i, x in enumerate(digits[::-1]):
            if carry == 0:
                break
            else:
                carry, x = divmod(x+carry, 10)
                digits[lens-i] = x
        if carry:
            digits.insert(0, carry)
        return digits


@pytest.mark.parametrize(('nums',  'ret'), [([1, 2, 3],  [1, 2,  4]),
                                            ([4, 3, 2, 1], [4, 3, 2, 2]),
                                            ([3, 2, 9], [3, 3, 0]),
                                            ([9], [1, 0])])
def test1(nums, ret):
    solution = Solution()
    a = list(nums)
    assert solution.plusOne1(a) == ret
    b = list(nums)
    assert solution.plusOne2(b) == ret
