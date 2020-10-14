#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest


class Solution:
    """
    单调栈：
    遍历数组，如果当前元素比栈顶元素大，则入栈; 否则不断弹出栈顶元素，使得左边数字最小    
    """

    def removeKdigits(self, num: str, k: int) -> str:
        if not num or k == len(num):
            return '0'

        stack = []
        for x in num:
            while k and stack and stack[-1] > x:
                stack.pop()
                k -= 1
            stack.append(x)

        # 如果弹出元素不满k个，由于当前栈内是单调递增的，直接去掉尾部的元素即可
        # case: '12435' 2
        if k:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'


@pytest.mark.parametrize(('nums', 'target', 'ret'), [('1432219', 3, '1219'),
                                                     ('10200', 1, '200'),
                                                     ('11200', 1, '1100'),
                                                     ('12345', 2, '123'),
                                                     ('12435', 2, '123'),
                                                     ('125432', 2, '1232'),
                                                     ('1234567890', 9, '0'),
                                                     ('4321', 4, '0'),
                                                     ('43210', 4, '0'),
                                                     ('210430', 2, '430'),
                                                     ('10', 2, '0')])
def test1(nums, target, ret):
    solution = Solution()
    assert solution.removeKdigits(nums, target) == ret
