#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def titleToNumber(self, s: str) -> int:
        """
        python内置函数：
        ord('a') = 97
        chr(97) = a

        m**n 求m的n次方，pow()函数可以开方
        """
        ret = 0
        for i, x in enumerate(s[::-1]):
            num = 26**i * (ord(x)-64)
            ret += num
        return ret


@pytest.mark.parametrize(("param", "ret"), [('A', 1),
                                            ('B', 2),
                                            ('C', 3),
                                            ('AA', 27),
                                            ('AB', 28),
                                            ('ZY', 701)])
def test1(param, ret):
    solution = Solution()
    assert solution.titleToNumber(param) == ret
