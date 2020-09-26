#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def letterCombinations(self, digits: str) -> list:
        """
        dfs回溯：使用path记录临时路径，当遍历到最后一个digit时，将path加入res中。
        """
        if not digits:
            return []
        num_map = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}
        res = []
        self.dfs(num_map, digits, 0, '', res)
        return res

    def dfs(self, num_map, digits, index, path, res):
        if index == len(digits):
            res.append(path)
            return
        for n in num_map.get(digits[index]):
            self.dfs(num_map, digits, index+1, path+n, res)


@pytest.mark.parametrize(("param", "ret"), [('23', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
                                            ('2', ['a', 'b', 'c'])])
def test1(param, ret):
    solution = Solution()
    assert set(solution.letterCombinations(param)) == set(ret)
