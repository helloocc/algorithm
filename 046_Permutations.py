#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    """
    另一种方法：内置itertools.permutations(nums)函数
    """

    def permute(self, nums: list) -> list:
        res = list()
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)


@pytest.mark.parametrize(('nums', 'res'), [([1, 2], [[1, 2],
                                                     [2, 1]]),
                                           ([1, 2, 3], [[1, 2, 3],
                                                        [1, 3, 2],
                                                        [2, 1, 3],
                                                        [2, 3, 1],
                                                        [3, 1, 2],
                                                        [3, 2, 1]])
                                           ])
def test1(nums, res):
    s = Solution()
    assert s.permute(nums) == res
