#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def groupAnagrams(self, strs: list) -> list:
        """
        首先排序字符串，再当成key存为dict。
        """
        res = dict()
        for st in strs:
            key = ''.join(sorted(st))
            res[key] = res.get(key, [])+[st]
        return list(res.values())


@pytest.mark.parametrize(('nums', 'ret'),
                         [(["eat", "tea", "tan", "ate", "nat", "bat"],
                           [["eat", "tea", "ate", ],
                            ["tan", "nat"],
                            ["bat"]]),

                          (["ab", "cd", "ba"],
                           [["ab", "ba"],
                            ["cd"]])])
def test1(nums,  ret):
    s = Solution()
    assert s.groupAnagrams(nums) == ret
