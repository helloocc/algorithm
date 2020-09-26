#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def isValid(self, s: str) -> bool:
        """
        注意把场景覆盖完整，用例要写全。
        """
        if not s:
            return True

        _map = {')': '(', '}': '{', ']': '['}
        stack = list()
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if stack:
                    if _map.get(ch) != stack.pop():
                        return False
                else:
                    return False
        return not stack


@pytest.mark.parametrize(('param',  'ret'), [('()', True),
                                             ('', True),
                                             ('(]', False),
                                             ('(', False),
                                             (']', False),
                                             ('))', False),
                                             ('((', False),
                                             ('()[{}]', True),
                                             ('()[]{}', True)])
def test1(param,  ret):
    solution = Solution()
    assert solution.isValid(param) == ret
