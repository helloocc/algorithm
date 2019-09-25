#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    """
    思想：如果子串是回文串，则从中心往两边扩展是相同的字符。
    需要考虑回文串是奇数'aba'和偶数'abba'的不同场景。
    """

    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            longest = max(longest, self.helper(s, i, i),
                          self.helper(s, i, i+1), key=len)
        return longest

    def helper(self, s, l, r):
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


@pytest.mark.parametrize(('input_str', 'output'), [('babad', 'bab'),
                                                   ('abccba', 'abccba'),
                                                   ('abc', 'a'),
                                                   ('', ''),
                                                   ('a', 'a'),
                                                   ('cbabd', 'bab'),
                                                   ('cbbd', 'bb')])
def test1(input_str, output):
    solution = Solution()
    assert solution.longestPalindrome(input_str) == output
