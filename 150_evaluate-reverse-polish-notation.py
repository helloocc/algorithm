#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    """
    python整除向下取整：
        6 //  132 = 0
        6 // -132 = -1
    """

    def evalRPN1(self, tokens: List[str]) -> int:
        """
        eval效率太低
        """
        stack = list()

        for token in tokens:
            if token in ('+', '-', '*', '/'):
                res = eval(stack.pop(-2) + token + stack.pop(-1))
                stack.append(str(int(res)))
            else:
                stack.append(token)
        return int(stack[-1])

    def evalRPN2(self, tokens: List[str]) -> int:
        op = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y),
        }
        stack = list()

        for token in tokens:
            if token in op:
                stack.append(op[token](stack.pop(-2), stack.pop(-1)))
            else:
                stack.append(int(token))
        return stack[-1]


@pytest.mark.parametrize(('param', 'ret'), [
    (["2", "1", "+", "3", "*"], 9),
    (["3", "-4", "+"], -1),
    (["4", "-2", "/", "2", "-3", "-", "-"], -7),
    (["4", "13", "5", "/", "+"], 6),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)])
def test1(param, ret):
    solution = Solution()
    assert solution.evalRPN1(param) == ret
    assert solution.evalRPN2(param) == ret
