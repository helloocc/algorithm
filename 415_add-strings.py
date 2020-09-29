#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        res = ''
        carry = 0
        while i >= 0 or j >= 0:
            x = ord(num1[i]) - ord('0') if i >= 0 else 0
            y = ord(num2[j]) - ord('0') if j >= 0 else 0
            carry, mod = divmod(x + y + carry, 10)
            # 逆序加，但结果按正常顺序存，即往前保存当前结果
            res = str(mod) + res
            i, j = i - 1, j - 1

        return str(carry) + res if carry else res


@pytest.mark.parametrize(('num1', 'num2', 'ret'), [
    ('5', '7', '12'),
    ('55', '77', '132'),
    ('200', '300', '500'),
    ('999', '1', '1000'),
    ('198', '10', '208'),
    ('1', '9', '10')])
def test1(num1, num2, ret):
    solution = Solution()
    assert solution.addStrings(num1, num2) == ret
