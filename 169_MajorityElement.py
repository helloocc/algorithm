#!/usr/bin/env python
# -*- coding=utf8 -*-

import pytest


class Solution:
    def majorityElement1(self, nums: list) -> int:
        dic = dict()
        lens = len(nums)/2
        for _, x in enumerate(nums):
            dic[x] = dic.get(x, 0)+1
            if dic.get(x) > lens:
                return x

    def majorityElement2(self, nums: list) -> int:
        """
        先排序再取中值，效率高！
        """
        nums.sort()
        return nums[len(nums)//2]


@pytest.mark.parametrize(("param", "ret"), [([3, 2, 3], 3),
                                            ([2, 1, 1], 1),
                                            ([2, 2, 2, 2, 1, 1, 1, 2, 2], 2)])
def test1(param, ret):
    s = Solution()
    copy1 = list(param)
    assert s.majorityElement1(copy1) == ret

    copy2 = list(param)
    assert s.majorityElement2(copy2) == ret
