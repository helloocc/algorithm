#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def merge(self, intervals: list) -> list:
        """
        先排序list，再依次比较区间。
        """
        res = []
        for num in sorted(intervals, key=lambda x: x[0]):
            if res and num[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], num[1])
            else:
                res.append(num)
        return res


@pytest.mark.parametrize(('nums', 'res'),
                         [([[1, 3], [2, 6], [8, 10], [15, 18]],
                           [[1, 6], [8, 10], [15, 18]]),

                          ([[1, 4], [4, 5]],
                           [[1, 5]]),

                          ([[1, 3], [2, 5], [0, 8]],
                           [[0, 8]]),

                          ([[1, 4], [0, 5], [5, 7]],
                           [[0, 7]]),

                          ([[1, 2], [4, 5], [6, 7]],
                           [[1, 2], [4, 5], [6, 7]])
                          ])
def test1(nums,  res):
    s = Solution()
    assert s.merge(nums) == res
