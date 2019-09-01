#!/usr/bin/env python
# -*- coding=utf8 -*-

import pytest


class Solution:
    def reverse(self, x: int) -> int:
        val = abs(x)
        op = (x > 0) - (x < 0)
        new_str = ''
        for i, j in enumerate(str(val)):
            new_str = j+new_str
        new_int = int(new_str)*op
        if -2**31 <= new_int <= 2**31:
            return new_int
        return 0

    def reverse1(self, x: int) -> int:
        """
        第一步：求符号
        第二步：step为-1切片，并求绝对值
        第三步：op*val恢复原始符号，val<2**31绝对值判断是否溢出，溢出乘以0则返回值为0

        切片操作：[start_index:  stop_index:  step]
        """
        op = (x > 0) - (x < 0)
        val = int(str(x*op)[::-1])
        return op*val * (val < 2**31)


@pytest.mark.parametrize(('param',  'ret'), [(123, 321),
                                             (-123, -321),
                                             (-120, -21),
                                             (120, 21)])
def test1(param, ret):
    solution = Solution()
    assert solution.reverse(param) == ret
    assert solution.reverse1(param) == ret
