#!/usr/bin/env python
#-*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    """
    DP思路:
    s[0:i]能拆分，说明总能找到k使得s[0:k]能拆成功，并且s[k:i]在字典中。
    dp[i]表示是s[0:i]是否能被拆分

    dp[0] = True 空字符串的场景
    dp[i] = dp[k] + (s[k:i] in dict)
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 要考虑空字符串的场景，所以+1
        dp = [False]*(len(s)+1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
        return dp[-1]


@pytest.mark.parametrize(('param1', 'param2', 'res'), [
    ("leetcode", ["leet", "code"], True),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ("applepenapple", ["apple", "pen"],True)
])
def test1(param1, param2, res):
    solution = Solution()
    assert solution.wordBreak(param1, param2) == res
