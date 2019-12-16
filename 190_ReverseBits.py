#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def reverseBits1(self, n: int) -> int:
        ret = 0
        for _ in range(32):
            ret = ret << 1 | n & 1
            n >>= 1
        return ret

    def reverseBits2(self, n: int) -> int:
        """
        bin(x)返回值str，bin(3)=0b11
        zfill(width): width指定字符串的长度。原字符串右对齐，前面填充0。
        """
        return int(bin(n)[2:].zfill(32)[::-1], 2)


@pytest.mark.parametrize(('param', 'ret'), [
    (int('00000010100101000001111010011100', 2),
     int('00111001011110000010100101000000', 2)),
    (int('11111111111111111111111111111101', 2), int('10111111111111111111111111111111', 2))])
def test1(param, ret):
    solution = Solution()
    assert solution.reverseBits1(param) == ret
    assert solution.reverseBits2(param) == ret
