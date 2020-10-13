#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest


class Solution:
    def minSteps(self, n: int) -> int:
        """
        找规律:
        1.可以被整除，则结果为 除数的最小步数 + copy/paste的次数
        2.不能被整除，则每次粘贴1个，结果为n
        """
        def dfs(n):
            if n == 0 or n == 1:
                return 0
            if n == 2:
                return 2
            for i in range(2, n)[::-1]:
                if n % i == 0:
                    res = dfs(i) + n // i
                    return res
            return n

        return dfs(n)


@pytest.mark.parametrize(('param', 'ret'), [(1, 0),
                                            (2, 2),
                                            (3, 3),
                                            (4, 4),
                                            (5, 5),
                                            (6, 5),
                                            (7, 7),
                                            (8, 6),
                                            (9, 6)])
def test1(param, ret):
    solution = Solution()
    assert solution.minSteps(param) == ret
