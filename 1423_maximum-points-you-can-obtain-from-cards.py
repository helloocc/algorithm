#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    def maxScore1(self, cardPoints: List[int], k: int) -> int:
        """
        DFS超时
        """
        if k == len(cardPoints):
            return sum(cardPoints)

        def dfs(cards, k, res):
            if k and cards:
                res += max(cards[0] + dfs(cards[1:], k - 1, res),
                           cards[-1] + dfs(cards[:-1], k - 1, res))
            return res

        return dfs(cardPoints, k, 0)

    def maxScore2(self, cardPoints: List[int], k: int) -> int:
        """
        逆向思维，求左右取得最大值，转化为个数为k的连续最小子数组
        滑动窗口进行求值
        """
        lens = len(cardPoints)
        if k == lens:
            return sum(cardPoints)

        cur = sum(cardPoints[:lens - k])
        min_ = cur
        l, r = 0, lens - k
        while r < lens:
            # 开始滑动窗口，每次左边滑出一个，右边滑进一个
            cur = cur - cardPoints[l] + cardPoints[r]
            min_ = min(cur, min_)
            l += 1
            r += 1

        return sum(cardPoints) - min_

    def maxScore3(self, cardPoints: List[int], k: int) -> int:
        """
        滑动窗口直接求左右取得最大值
        """
        if k == len(cardPoints):
            return sum(cardPoints)

        # 初始为右边k个数的和
        cur = sum(cardPoints[-k:])
        max_ = cur
        for i in range(k):
            # 每次左边滑进一个，右边滑出一个
            cur += cardPoints[i] - cardPoints[i - k]
            max_ = max(cur, max_)
        return max_


@pytest.mark.parametrize(('nums', 'target', 'ret'), [
    ([100, 40, 17, 9, 73, 75], 3, 248),
    ([96, 90, 41, 82, 39, 74, 64, 50, 30], 8, 536),
    ([1, 79, 80, 1, 1, 1, 200, 1], 3, 202),
    ([1, 2, 3, 4, 5, 6, 1], 3, 12),
    ([9, 7, 7, 9, 7, 7, 9], 7, 55),
    ([2, 2, 2], 2, 4)])
def test1(nums, target, ret):
    solution = Solution()
    assert solution.maxScore1(nums, target) == ret
    assert solution.maxScore2(nums, target) == ret
    assert solution.maxScore3(nums, target) == ret
