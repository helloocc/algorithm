#!/usr/bin/env python
#-*- coding=utf8 -*-
import pytest


class Solution:
    """
    类似题目005最长回文子串
    思想：从中心往两边扩展是相同的字符，需要考虑回文串是奇数'aba'和偶数'abba'的不同场景
    """

    def countSubstrings1(self, s: str) -> int:
        num = 0
        for i in range(len(s)):
            # 回文是奇数
            num += self.count(i, i, s)
            # 回文是偶数
            num += self.count(i, i+1, s)
        return num

    def count(self, l, r, s):
        num = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            num += 1
            l -= 1
            r += 1
        return num

    def countSubstrings2(self, s: str) -> int:
        """
        len(s)*2-1推算：
        假设s为3：
        0 0    0//2 0//2
        0 1    1//2 2//2
        1 1    2//2 3//2
        1 2    3//2 4//2
        2 2    4//2 5//2
        """
        num = 0
        for i in range(len(s)*2-1):
            l = i//2
            r = (i+1)//2
            while l >= 0 and r < len(s) and s[l] == s[r]:
                num += 1
                l -= 1
                r += 1
        return num


@pytest.mark.parametrize(("param", "ret"), [('abc', 3),
                                            ('aaa', 6),
                                            ('aba', 4),
                                            ('b', 1)])
def test1(param, ret):
    solution = Solution()
    assert solution.countSubstrings1(param) == ret
    assert solution.countSubstrings2(param) == ret
