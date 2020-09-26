#!/usr/bin/env python
# -*- coding=utf8 -*-
from math import sqrt
from collections import deque
import pytest


class Solution:
    """
    四平方定理： 任何一个正整数都可以表示成不超过四个整数的平方之和。
    推论：满足四数平方和定理的数n（四个整数的情况），必定满足 n = 4 ^ a * (8b + 7)
    """

    def numSquares1(self, n: int) -> int:
        """
        DP: 类似题目322 coin change. 本题的'coin'就是平方数
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            # 优化j的取值否则超时。j取值不大于i的开方
            for j in range(1, int(sqrt(i)) + 1):
                square = j * j
                if i >= square:
                    dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]

    def numSquares2(self, n: int) -> int:
        """
        DFS会超时
        """
        memo = dict()

        def dfs(target):
            if target in memo:
                return memo[target]
            if target < 4:
                return target
            count = float('inf')
            for i in range(int(sqrt(target)) + 1, 1, -1):
                if target >= i * i:
                    count = min(count, dfs(target - i * i) + 1)
                    memo[target] = count
            return count

        return dfs(n)

    def numSquares3(self, n: int) -> int:
        """
        BFS：类似于寻找最短路径
        从根节点开始像下逐层延伸，每次延伸的元素是各个平方数
        """
        queue = deque()
        queue.append([n, 0])
        visited = [False] * (n + 1)
        path = 0

        while queue:
            remain, path = queue.popleft()
            if not visited[remain]:
                for i in range(int(sqrt(remain) + 1))[::-1]:
                    # 当遇到第一个刚好满足的平方数时，就是最短路径
                    if remain == i * i:
                        return path + 1
                    if remain > i * i:
                        queue.append([remain - i * i, path + 1])
                        visited[remain] = True
        return path


@pytest.mark.parametrize(('param', 'ret'), [(12, 3),
                                            (1, 1),
                                            (4, 1),
                                            (5, 2),
                                            (8, 2),
                                            (9, 1),
                                            (7691, 3),
                                            (39, 4),
                                            (13, 2)])
def test1(param, ret):
    solution = Solution()
    assert solution.numSquares1(param) == ret
    assert solution.numSquares2(param) == ret
    assert solution.numSquares3(param) == ret
