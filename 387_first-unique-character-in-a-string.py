#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest


class Solution:
    def firstUniqChar1(self, s: str) -> int:
        if not s:
            return -1
        memo = dict()
        index = dict()
        for i, x in enumerate(s):
            if x not in memo:
                memo[x] = 1
                index[x] = i
            else:
                if x in index:
                    index.pop(x)
        return min(index.values()) if index else -1

    def firstUniqChar2(self, s: str) -> int:
        from collections import Counter
        if not s:
            return -1
        count = Counter(s)
        if min(count.values()) != 1:
            return -1
        for k in count:
            if count[k] == 1:
                return s.index(k)


@pytest.mark.parametrize(('param', 'ret'), [('leetcode', 0),
                                            ('loveleetcode', 2),
                                            ('llli', 3),
                                            ('liial', 3),
                                            ('abcabcd', 6),
                                            ('abcabc', -1),
                                            ('', -1)])
def test1(param, ret):
    solution = Solution()
    assert solution.firstUniqChar1(param) == ret
    assert solution.firstUniqChar2(param) == ret
