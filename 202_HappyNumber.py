#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def isHappy1(self, n: int) -> bool:
        """
        最终如果是0,1,4，会陷入循环
        """
        while n not in [0, 1, 4]:
            cur, n = n, 0
            for x in str(cur):
                x = int(x)
                n += x*x
        if n == 1:
            return True
        else:
            return False

    def isHappy2(self, n: int) -> bool:
        """
        记录已经出现过的数字，如果再次出现则形成死循环。
        """
        seen = set()
        while n not in seen:
            seen.add(n)
            # ord相比int函数速度快
            n = sum((ord(x)-ord('0')) ** 2 for x in str(n))
        return n == 1


@pytest.mark.parametrize(("num", "res"), [(19, True),
                                          (2, False),
                                          (1, True)])
def test1(num, res):
    s = Solution()
    assert s.isHappy1(num) == res
    assert s.isHappy2(num) == res
