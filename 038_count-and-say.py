#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest
"""
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
 10.   13211311123113112211
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        """
        递归
        """
        if n == 1:
            return '1'
        pre = self.countAndSay(n-1)
        res = ''
        target, count = pre[0], 0
        for _, x in enumerate(pre):
            if x == target:
                count += 1
            else:
                res += (str(count)+target)
                target, count = x, 1
        res += (str(count)+target)
        return res


@pytest.mark.parametrize(('param', 'res'), [(1, '1'),
                                            (2, '11'),
                                            (3, '21'),
                                            (4, '1211'),
                                            (6, '312211')])
def test1(param, res):
    s = Solution()
    assert s.countAndSay(param) == res
