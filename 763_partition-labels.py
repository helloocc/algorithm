#!/usr/bin/env python
#-*- coding=utf8 -*-

from typing import List
import pytest


class Solution:
    """
    思路：
    1.用字典记录所有字符的最右索引
    2.遍历S，判断当前最右索引和字符的最右索引
    3.如果二者相等，则可以拆分
    """
    def partitionLabels(self, S: str) -> List[int]:
        res = []
        rightmost = {c: i for i, c in enumerate(S)}

        left, right = 0, 0
        for i, x in enumerate(S):
            right = max(rightmost[x], right)
            if i == right:
                res += [right-left+1]
                left = i+1
        return res


@pytest.mark.parametrize(('param1',  'ret'), [('Kick', [1, 1, 1, 1]),
                                              ('ababcbacadefegdehijhklij',[9, 7, 8]),
                                              ('leetcode', [1, 7]),
                                              ('ijddacfafh', [1, 1, 2, 5, 1])])
def test1(param1,  ret):
    s = Solution()
    assert s.partitionLabels(param1) == ret
