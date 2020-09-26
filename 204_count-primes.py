#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    """
    埃拉托斯特尼筛法:
    https://zh.wikipedia.org/wiki/%E5%9F%83%E6%8B%89%E6%89%98%E6%96%AF%E7%89%B9%E5%B0%BC%E7%AD%9B%E6%B3%95
    """

    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        flag = [1]*n
        flag[0] = flag[1] = 0

        # 只需遍历[2,根号n],因为超过根号n,已经作为因子i在前面被筛掉了
        for i in range(2, int(n**0.5)+1):
            if flag[i]:
                # 筛掉i的倍数
                flag[i*i:n:i] = [0]*len(range(i*i, n, i))
        return sum(flag)


@pytest.mark.parametrize(('num', 'ret'), [(10, 4),
                                          (2, 0),
                                          (4, 2)])
def test1(num, ret):
    solution = Solution()
    assert solution.countPrimes(num) == ret
