#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest


class Solution:
    def decodeString1(self, s: str) -> str:
        """
        辅助栈：当前次数和当前字符串以数组形式入栈，遇到特定字符时出栈计算
        """
        # 以字符串形式记录次数，前面补位0
        num = '0'
        stack = [[num, '']]
        for x in s:
            if x.isdigit():
                num += x
            elif x.isalpha():
                stack[-1][1] += x
            elif x == '[':
                stack.append([num, ''])
                # 遇到'['时次数重置为0
                num = '0'
            elif x == ']':
                count, cur = stack.pop()
                # 次数转换成int时，如果是补位0，则转换成1
                count = 1 if not int(count) else int(count)
                stack[-1][1] += count * cur
        return stack[-1][1]

    def decodeString2(self, s: str) -> str:
        """
        递归
        """

        def dfs(idx):
            res, num = '', 0
            while idx < len(s):
                x = s[idx]
                if x.isdigit():
                    num = num * 10 + int(x)
                elif x.isalpha():
                    res += x
                elif x == '[':
                    cur, idx = dfs(idx + 1)
                    res += (num * cur)
                    num = 0
                elif x == ']':
                    return res, idx
                idx += 1
            return res

        return dfs(0)


@pytest.mark.parametrize(('param', 'ret'), [
    ('2[a]2[bc]', 'aabcbc'),
    ('3[a2[c]]', 'accaccacc'),
    ('2[abc]3[cd]ef', 'abcabccdcdcdef'),
    ('10[le]', 'lelelelelelelelelele'),
    ('abc3[cd]xyz', 'abccdcdcdxyz')])
def test1(param, ret):
    solution = Solution()
    assert solution.decodeString1(param) == ret
    assert solution.decodeString2(param) == ret
