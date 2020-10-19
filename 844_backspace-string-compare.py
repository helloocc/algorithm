#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest


class Solution:
    def backspaceCompare1(self, S: str, T: str) -> bool:
        """
        常规解法，利用栈，时间空间复杂度都是O(S+T)即O(n)
        """
        def parse(st):
            stack = []
            for x in st:
                if x == '#' and stack:
                    stack.pop()
                elif x.isalpha():
                    stack.append(x)
            return stack

        return parse(S) == parse(T)

    def backspaceCompare2(self, S: str, T: str) -> bool:
        """
        Follow up: 要求空间复杂度O(1)，双指针逆序遍历
        """
        i, j, del1, del2 = len(S) - 1, len(T) - 1, 0, 0
        while i >= 0 or j >= 0:
            #  逆序删除S
            while i >= 0:
                if S[i] == '#':
                    i -= 1
                    del1 += 1
                elif del1:
                    i -= 1
                    del1 -= 1
                else:
                    break

            # 逆序删除T
            while j >= 0:
                if T[j] == '#':
                    j -= 1
                    del2 += 1
                elif del2:
                    j -= 1
                    del2 -= 1
                else:
                    break

            if i >= 0 and j >= 0:
                if S[i] == T[j]:
                    i -= 1
                    j -= 1
                else:
                    return False
            elif i >= 0 or j >= 0:
                return False

        return True


@pytest.mark.parametrize(('param1', 'param2', 'ret'), [
    ('ab#c', 'ad#c', True),
    ('ab##', 'c#d#', True),
    ('a##c', '#a#c', True),
    ('a###c', '#a#d#c', True),
    ('nzp#o#g', 'b#nzp#o#g', True),
    ('a#c', 'b', False),
    ('#', 'b', False)])
def test1(param1, param2, ret):
    solution = Solution()
    assert solution.backspaceCompare1(param1, param2) == ret
    assert solution.backspaceCompare2(param1, param2) == ret
