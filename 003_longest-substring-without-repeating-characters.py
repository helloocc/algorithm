#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        """
        滑动窗口，i,j不停滑动。
        当j遇到的字符没有出现过，则记录当前字符，j继续向前移动。
        当碰到出现过的字符时，从记录的set中移除s[i]，i向前移动。
        """
        i = j = max_num = 0
        used = set()
        while i < len(s) and j < len(s):
            if s[j] in used:
                used.remove(s[i])
                i += 1
            else:
                used.add(s[j])
                j += 1
                max_num = max(max_num, j-i)
        return max_num

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        滑动窗口优化：使用字典记录出现过的字符及其索引。
        1. 如果字符出现过，则start从出现过的索引+1开始重新计算。
           需要增加判断start是否比出现的索引要小，例：'tmmzuxt'，判断第二个t时，t出现索引为0，此时start=2大于0，不应该符合条件+1。
        2. 如果字符没有出现过，则计算一次max_num。

        记住：不管字符出现与否，每次都要更新字典记录的最新索引值。
        """
        used = dict()
        max_num = start = 0
        for i, c in enumerate(s):
            if c in used.keys() and start <= used.get(c):
                start = used.get(c)+1
            else:
                max_num = max(max_num, i-start+1)
            used[c] = i
        return max_num


@pytest.mark.parametrize(("param", "ret"), [('abcabcbb', 3),
                                            ('dvdfe', 4),
                                            ('abcdbef', 5),
                                            ('abcdeblbf', 5),
                                            ('dwwefw', 3),
                                            ('tmmzuxt', 5),
                                            ('bbb', 1)])
def test1(param, ret):
    solution = Solution()
    assert solution.lengthOfLongestSubstring(param) == ret
