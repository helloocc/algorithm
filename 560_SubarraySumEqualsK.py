#!/usr/bin/env python
#-*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    """
    求连续子数组的和，直接用暴力破解，穷举出所有子数组，算出和等于k即可。
    如何求子数组的和sum(i,j)？ 暴力法需要重复多次计算，而使用前缀和记录则是O(1)
    即：sum(i,j) = sum(0,j) - sum(0,i-1)

    index:      0  1  2  4
    nums:     [ 1, 2, 1, 3 ]
    sum:     0, 1, 3, 4, 7    补位0，num==k的场景
    """

    def subarraySum1(self, nums: List[int], k: int) -> int:
        """
        前缀和：会超时，仅提供思路
        """
        sums=[0]
        for x in nums:
            sums.append(sums[-1]+x)

        count = 0
        for j in range(len(sums)):
            for i in range(j):
                if sums[j]-sums[i] == k:
                    count += 1
        return count


    def subarraySum2(self, nums: List[int], k: int) -> int:
        """
        前缀和+hash表优化:

        问题转化为: 求i<j，满足sum(i) = sum(j) - k
        对于每个j，记录之前所有的presum，然后查找有多少个presum==sum(j)-k
        """
        count, sums = 0, 0
        dic = {0: 1}
        for x in nums:
            sums += x
            count += dic.get(sums-k, 0)
            dic[sums] = dic.get(sums, 0)+1
        return count


@pytest.mark.parametrize(('nums', 'k', 'res'), [([1, 1, 1], 2, 2),
                                                ([1, 2, 1, 3], 3, 3),
                                                ([1, 1, 1, -2, 1, 1], 3, 2),
                                                ([2, 4, -2], 2, 2),
                                                ([2, 4, -2], 0, 0),
                                                ([1, 2, 3], 1, 1)])
def test1(nums, k, res):
    s = Solution()
    assert s.subarraySum1(nums, k) == res
    assert s.subarraySum2(nums, k) == res
