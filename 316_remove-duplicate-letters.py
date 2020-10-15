#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest
import collections


class Solution:
    def removeDuplicateLetters1(self, s: str) -> str:
        """
        类似单调栈：
        1.参考题解402. 本题中的letter的移除个数取决于重复的次数
        2.遍历字符串，对于每个字符:
            a.已经在栈中，则无需继续判断，直接丢弃
            b.不在栈中，如果栈顶元素字典序更大且后面还会出现，则丢弃栈顶元素
        3.每遍历一个字符，其剩余出现次数-1
        """
        remain = collections.Counter(s)
        stack = list()
        for c in s:
            if c not in stack:
                while stack and stack[-1] > c and remain[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain[c] -= 1
        return ''.join(stack)

    def removeDuplicateLetters2(self, s: str) -> str:
        """
        记录每个字符最右的索引，用于是否从栈中弹出
        """
        rindex = {x: i for i, x in enumerate(s)}
        stack = list()

        for i, x in enumerate(s):
            if x not in stack:
                while stack and stack[-1] > x and rindex[stack[-1]] > i:
                    stack.pop()
                stack.append(x)
        return ''.join(stack)


@pytest.mark.parametrize(('param', 'ret'), [('bcabc', 'abc'),
                                            ('cbacdcbc', 'acdb'),
                                            ('cdadabcc', 'adbc'),
                                            ('cbdbcd', 'bcd'),
                                            ('cbac', 'bac'),
                                            ('aabc', 'abc')])
def test1(param, ret):
    solution = Solution()
    assert solution.removeDuplicateLetters1(param) == ret
    assert solution.removeDuplicateLetters2(param) == ret
