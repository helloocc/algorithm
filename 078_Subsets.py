#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def subsets(self, nums: list) -> list:
        """
        Iteratively
        迭代：每次新增数字都是遍历前一结果，并增加带有新数字的子数组。
        """
        res = list()
        res.append([])
        for num in nums:
            #  new = list()
            #  for li in res:
            #      new.append(li+[num])
            #  res.extend(new)
            res += [item+[num] for item in res]
        return res


@pytest.mark.parametrize(('param,ret'), [([1, 2, 3], [[],
                                                      [1],
                                                      [2],
                                                      [1, 2],
                                                      [3],
                                                      [1, 3],
                                                      [2, 3],
                                                      [1, 2, 3]]),
                                         ([1, 2], [[],
                                                   [1],
                                                   [2],
                                                   [1, 2]]),
                                         ([1], [[], [1]])])
def test(param, ret):
    s = Solution()
    assert s.subsets(param) == ret
