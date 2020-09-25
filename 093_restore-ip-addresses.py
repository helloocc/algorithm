#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        典型dfs+回溯
        """
        res = []

        def dfs(s, path):
            if not s and len(path) == 4:
                res.append('.'.join(path))
                return
            if not s or len(path) > 4:
                return

            dfs(s[1:], path + [s[0]])
            # 这里记得判断s长度，如果s长度为1，则s[:1],s[:2],s[:3]都等于s
            if len(s) >= 2 and s[0] != '0':
                dfs(s[2:], path + [s[:2]])
                if len(s) >= 3 and int(s[:3]) <= 255:
                    dfs(s[3:], path + [s[:3]])

            return res

        dfs(s, [])
        return res


@pytest.mark.parametrize(('param', 'ret'), [
    ("25525511135", ["255.255.11.135", "255.255.111.35"]),
    ("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
    ("0000", ["0.0.0.0"]), ("1111", ["1.1.1.1"]),
    ("010010", ["0.10.0.10", "0.100.1.0"])])
def test1(param, ret):
    solution = Solution()
    assert solution.restoreIpAddresses(param) == ret
