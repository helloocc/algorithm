#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def moveZeroes1(self, nums: list) -> None:
        """
        逆序解决数组乱序问题。
        """
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        return nums

    def moveZeroes2(self, nums: list) -> None:
        """
        学习 key=bool 用法.
        """
        nums.sort(key=bool, reverse=True)
        return nums

    def moveZeroes3(self, nums: list) -> None:
        """
        看似简单，想半天想不明白的解法，希望有朝一日能彻底理解。
        """
        zero = 0
        for non_zero in range(len(nums)):
            if nums[non_zero] != 0:
                nums[zero], nums[non_zero] = nums[non_zero], nums[zero]
                zero += 1
        return nums


@pytest.mark.parametrize(('nums', 'ret'), [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
                                           ([0, 0, 0, 1], [1, 0, 0, 0]),
                                           ([4, 5, 0, 6], [4, 5, 6, 0])])
def test1(nums, ret):
    s = Solution()
    copy1 = list(nums)
    assert s.moveZeroes1(copy1) == ret

    copy2 = list(nums)
    assert s.moveZeroes2(copy2) == ret

    copy3 = list(nums)
    assert s.moveZeroes3(copy3) == ret
