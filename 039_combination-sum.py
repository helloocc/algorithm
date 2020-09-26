#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        """
        DFS: 使用path记录路径，如果符合则加入res.
        """
        candidates.sort()
        res = list()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)


@pytest.mark.parametrize(('nums', 'target', 'res'), [([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
                                                     ([3, 4, 5], 6, [[3, 3]]),
                                                     ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]])])
def test1(nums, target, res):
    s = Solution()
    assert s.combinationSum(nums, target) == res
