#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
import pytest


class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        """
        单调栈：
        求以A[i]为最小元素的子数组个数，则可以求以A[i]为最小元素的最长子数组。
        假设A[i]左边第一个小于A[i]的元素为A[left]，右边第一个小于A[i]的元素为A[right]
        则子数组个数 n[i]= (i-left)*(right-i) (排列组合，左边有i-left种选择，右边有right-i种选择)
        最终结果为 A[i]*n[i]
        """
        if not A:
            return 0
        left = [0] * len(A)
        right = [0] * len(A)

        # 从左往右遍历，单调递增栈求数组中每个元素左边第一个小于它的数的索引
        stack = []
        for i in range(len(A)):
            # stack中存的是索引
            while stack and A[stack[-1]] > A[i]:
                stack.pop()
            # 左边没有比当前数小，则默认索引是-1: i-(-1)
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        # 从右往左遍历，单调递增栈求数组中每个元素右边第一个小于它的数的索引
        stack = []
        for i in range(len(A))[::-1]:
            # >= 处理相等场景
            while stack and A[stack[-1]] >= A[i]:
                stack.pop()
            # 右边没有比当前数小，则默认索引是len(A)
            right[i] = stack[-1] - i if stack else len(A) - i
            stack.append(i)

        res = 0
        for i in range(len(A)):
            res += left[i] * right[i] * A[i]
        return res % (10**9 + 7)


@pytest.mark.parametrize(('param', 'ret'), [([3, 1, 2, 4], 17),
                                            ([71, 55, 82, 55], 593),
                                            ([1, 2, 3], 10),
                                            ([1, 2], 4),
                                            ([1], 1),
                                            ([], 0)])
def test1(param, ret):
    solution = Solution()
    assert solution.sumSubarrayMins(param) == ret
