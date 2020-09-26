#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def maxArea(self, height: list) -> int:
        """
        贪心：面积受长和高的影响，当长度减小时，确保高度尽可能大，所以每次对高度更低的那个移动指针
        """
        max_area, p, q = 0, 0, len(height)-1
        while p < q:
            if height[p] < height[q]:
                max_area = max(max_area, height[p]*(q-p))
                p += 1
            else:
                max_area = max(max_area, height[q]*(q-p))
                q -= 1
        return max_area


@pytest.mark.parametrize(("param", "ret"), [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
                                            ([1, 2, 3], 2),
                                            ([2, 3, 4, 5, 18, 17, 6], 17),
                                            ([3, 3], 3),
                                            ([2, 2, 3], 4)])
def test1(param, ret):
    s = Solution()
    assert s.maxArea(param) == ret
