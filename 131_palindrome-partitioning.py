#!/usr/bin/env python
# -*- coding: utf8 -*-
from typing import List
import pytest


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """典型DFS"""
        res = []

        def dfs(s, path):
            if not s:
                res.append(path)
                return
            for i in range(1, len(s) + 1):
                head = s[:i]
                # 先判断前面字段是否回文，再判断剩下的字段是否回文
                if head == head[::-1]:
                    dfs(s[i:], path + [head])
        dfs(s, [])
        return res


@pytest.mark.parametrize(('param', 'ret'), [
    ('aab', [['a', 'a', 'b'],
             ['aa', 'b']]),
    ('a', [['a']]),
    ('aabb', [['a', 'a', 'b', 'b'],
              ['a', 'a', 'bb'],
              ['aa', 'b', 'b'],
              ['aa', 'bb']])
])
def test1(param, ret):
    solution = Solution()
    assert solution.partition(param) == ret
