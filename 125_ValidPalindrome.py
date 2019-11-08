#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        pythonic: ss = [c.lower() for c in s if c.isalnum()]
        """
        if not s:
            return True
        ss = ''
        for i in s:
            if i.isalnum():
                ss += i.lower()
        return ss == ss[::-1]


@pytest.mark.parametrize(('param', 'res'), [('A man, a plan, a canal: Panama', True),
                                            ('ab', False),
                                            ('0P', False),
                                            ('a', True),
                                            ('race a car', False)])
def test1(param, res):
    s = Solution()
    assert s.isPalindrome(param) == res
