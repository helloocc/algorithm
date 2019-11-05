#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest


class Solution:
    def romanToInt1(self, s: str) -> int:
        """
        思想：只有六种情况是两数相减，其他都是加上value即可。

        注：字符串s[i:i+1]只取一个字符，s[i:i+2]才是取两个字符。
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num_list = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']

        res, i, lens = 0, 0, len(s)
        while i < lens:
            if i == lens-1:
                res += dic.get(s[i])
                break
            if s[i:i+2] in num_list:
                temp = dic.get(s[i+1])-dic.get(s[i])
                res += temp
                i += 2
            else:
                res += dic.get(s[i])
                i += 1
        return res

    def romanToInt2(self, s: str) -> int:
        """
        取巧法：将减法场景全部替换为加法场景。
        """
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        s = s.replace("IV", "IIII").replace("IX", "VIIII")\
             .replace("XL", "XXXX").replace("XC", "LXXXX")\
             .replace("CD", "CCCC").replace("CM", "DCCCC")

        res = 0
        for c in s:
            res += dic[c]
        return res


@pytest.mark.parametrize(("param", "res"), [('III', 3),
                                            ('IV', 4),
                                            ('MCDLXXVI', 1476),
                                            ('IX', 9),
                                            ('LVIII', 58),
                                            ('MCMXCIV', 1994)])
def test1(param, res):
    s = Solution()
    assert s.romanToInt1(param) == res
    assert s.romanToInt2(param) == res
