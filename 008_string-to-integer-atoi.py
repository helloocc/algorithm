#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest


class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0

        st = str.strip()
        res, signed = 0, 0
        for i, x in enumerate(st):
            if not i and x in ['+', '-']:
                # '+'对应43  ','对应44  '-'对应45
                signed = -(ord(x) - ord(','))
            elif x.isdigit():
                res = res * 10 + int(x)
            else:
                break

        # 判断是否溢出
        if signed < 0:
            return max(res * signed, -2**31)
        else:
            return min(res, 2**31 - 1)


@pytest.mark.parametrize(('param', 'ret'), [("42", 42),
                                            ("  -42", -42),
                                            ("2147483648", 2147483647),
                                            ("2147483647", 2147483647),
                                            ("-2147483647", -2147483647),
                                            ("-2147483648", -2147483648),
                                            ("", 0),
                                            ("  +0 123", 0),
                                            (" +0a32", 0),
                                            ("3.14159", 3),
                                            ("+-2", 0),
                                            ("0-1", 0),
                                            (".1", 0),
                                            ("words and 987", 0),
                                            ("-91283472332", -2147483648),
                                            ("4193 with words", 4193)])
def test1(param, ret):
    solution = Solution()
    assert solution.myAtoi(param) == ret
