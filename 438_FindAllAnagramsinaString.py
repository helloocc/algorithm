#!/usr/bin/env python
#-*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    def findAnagrams1(self, s: str, p: str) -> List[int]:
        """
        子符串排序比较
        """
        res = list()
        p = sorted(list(p))
        lens = len(p)
        for i in range(len(s)-lens+1):
            if p == sorted(list(s[i:i+lens])):
                res.append(i)
        return res

    def findAnagrams2(self, s: str, p: str) -> List[int]:
        """
        滑动窗口
        """
        from collections import Counter
        res, window = list(), dict()
        need = Counter(p)
        left, right, length = 0, 0, len(p)
        while right < len(s):
            ch = s[right]
            # 遇到不需要字符时，重新开始计算
            if ch not in need:
                window.clear()
                left = right = right+1
            else:
                window[ch] = window.get(ch, 0)+1
                # 长度达到目标，判断并操作左指针
                if right-left+1 == length:
                    if window == need:
                        res.append(left)
                    window[s[left]] -= 1
                    left += 1
                # 每次遍历右指针右移一位
                right += 1
        return res


@pytest.mark.parametrize(("param1", "param2", "ret"), [
    ('cbaebabacd',  'abc', [0, 6]),
    ('ab', 'a', [0]),
    ('ab', 'c', []),
    ('abab', 'ab', [0, 1, 2])])
def test1(param1, param2, ret):
    solution = Solution()
    assert solution.findAnagrams1(param1, param2) == ret
    assert solution.findAnagrams2(param1, param2) == ret
