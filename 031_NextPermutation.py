#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    """
    理解题目：全排列数字中找出比当前数大一点的那个。

    以[6,5,4,8,7,5,1]为例：
    1.先从后往前找，8,7,5,1都是降序排列，我们先找到出现升序的那个地方。即num[2]和num[3]，此时我们假设index的值为3。
    2.从后往前，在num[index]~num[len-1]中找到比num[2]大的最小数，下标记为exchangeIndex。
    3.交换num[index-1]和num[exchangeIndex]的值。
    4.调整num[index]~num[len-1]为升序序列。
    """

    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens, index = len(nums), 0
        for i in range(1, lens)[::-1]:
            if nums[i] > nums[i-1]:
                index = i
                break
        if not index:
            nums.reverse()
        else:
            j = index-1
            for i in range(index, lens)[::-1]:
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
            nums[index:] = sorted(nums[index:])
        return nums


@pytest.mark.parametrize(('nums', 'res'), [([1, 2, 3], [1, 3, 2]),
                                           ([3, 2, 1], [1, 2, 3]),
                                           ([1, 3, 2], [2, 1, 3]),
                                           ([1, 5, 1], [5, 1, 1]),
                                           ([1, 3, 2, 3], [1, 3, 3, 2]),
                                           ([1, 3, 2, 4], [1, 3, 4, 2]),
                                           ([1, 4, 3, 2], [2, 1, 3, 4]),
                                           ([6, 1, 2, 5, 4], [6, 1, 4, 2, 5]),
                                           ([1, 1, 5], [1, 5, 1])])
def test1(nums, res):
    s = Solution()
    assert s.nextPermutation(nums) == res
