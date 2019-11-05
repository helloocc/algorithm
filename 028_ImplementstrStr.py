#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        注意异常场景。range(lens1-lens2+1)可代入实际数据思考。
        """
        if not needle:
            return 0
        lens1, lens2 = len(haystack), len(needle)
        if lens1 < lens2:
            return -1
        for i in range(lens1-lens2+1):
            if haystack[i:i+lens2] == needle:
                return i
        return -1


@pytest.mark.parametrize(('str1', 'str2', 'res'), [('hello', 'll', 2),
                                                   ('heoll', 'll', 3),
                                                   ('a', 'a', 0),
                                                   ('bbbba', 'a', 4),
                                                   ('abbbba', 'ab', 0),
                                                   ('', 'a', -1),
                                                   ('aaaaa', 'bba', -1)])
def test1(str1, str2, res):
    s = Solution()
    assert s.strStr(str1, str2) == res
