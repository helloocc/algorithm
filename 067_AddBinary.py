#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def addBinary1(self, a: str, b: str) -> str:
        carry, result = 0, ''

        a, b = list(a), list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            # 位数值
            result += str(carry % 2)
            # 进位数
            carry //= 2

        # 从末尾开始记录值，结果需要反转
        return result[::-1]

    def addBinary2(self, a: str, b: str) -> str:
        """
        int(x,base=10), bin(x)返回x的二进制表示

        int('11',2)=3   bin(4)=0b100
        """
        return bin(int(a, 2)+int(b, 2))[2:]


@pytest.mark.parametrize(("a", "b", "ret"), [('11', '1', '100'), ('1010', '1011', '10101')])
def test1(a, b, ret):
    solution = Solution()
    assert solution.addBinary1(a, b) == ret
    assert solution.addBinary2(a, b) == ret
