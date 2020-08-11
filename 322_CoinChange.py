#!/usr/bin/env python
# -*- coding=utf8 -*-


from typing import List
import pytest


class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        """
        DP: 自下而上
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if amount >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1

    def coinChange2(self, coins: List[int], amount: int) -> int:
        """
        自顶向下递归 + dict优化
        """
        memo = dict()

        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0

            res = float('inf')
            for coin in coins:
                if amount >= coin:
                    res = min(res, dfs(amount - coin) + 1)
                    memo[amount] = res
            return res

        res = dfs(amount)
        return res if res < float('inf') else -1

    def coinChange3(self, coins: List[int], amount: int) -> int:
        """
        贪心 + 剪枝
        1.想要总硬币数最少，肯定是优先用大面值硬币，所以对 coins 按从大到小排序
        2.先选大硬币，超过总额时，回溯选稍小面值的硬币
        """
        coins.sort(reverse=True)

        def dfs(coins, amount, count, res):
            if not coins:
                return res
            if amount % coins[0] == 0:
                # 满足要求
                res = min(res, count + amount // coins[0])
                return res
            else:
                # 不满足，回溯减少大硬币数量
                for i in range(amount // coins[0], -1, -1):
                    # 如果当前数量大于现有的，剪枝
                    if count + i > res:
                        break
                    res = dfs(coins[1:], amount - i * coins[0], count + i, res)
            return res

        res = dfs(coins, amount, 0, float('inf'))
        return res if res < float('inf') else -1


@pytest.mark.parametrize(('nums', 'target', 'ret'), [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1, 4, 5], 29, 6),
    ([186, 419, 83, 408], 6249, 20),
    ([1, 2, 3], 4, 2)])
def test1(nums, target, ret):
    solution = Solution()
    assert solution.coinChange1(nums, target) == ret
    assert solution.coinChange2(nums, target) == ret
    assert solution.coinChange3(nums, target) == ret
