#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    """
    backtracking解释：www.1point3acres.com/bbs/thread-172641-1-1.html
    """

    def generateParenthesis(self, n: int):
        res = list()
        self.dfs(n, n, '', res)
        return res

    def dfs(self, left, right, path, res):
        if left > right or left < 0 or right < 0:
            return
        if left == right == 0:
            res.append(path)
        self.dfs(left-1, right, path+'(', res)
        self.dfs(left, right-1, path+')', res)


@pytest.mark.parametrize(("param", "res"), [(1, ["()"]),
                                            (2, ["()()", "(())"]),
                                            (3, ["((()))",
                                                 "(()())",
                                                 "(())()",
                                                 "()(())",
                                                 "()()()"])
                                            ])
def test1(param, res):
    s = Solution()
    assert set(s.generateParenthesis(param)) == set(res)
