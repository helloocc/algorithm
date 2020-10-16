#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        前提条件：只有正数和负数相遇，才可能碰撞（负数和正数就不行）

        利用栈，遍历数组：
        1. 当前为负数且栈顶为正数时，进行碰撞判断
        2. 其他情况则直接入栈
        """
        stack = []
        for x in asteroids:
            while stack and x < 0 < stack[-1]:
                top = stack[-1]
                # 栈顶小于或等于当前负数时，栈顶弹出，负数继续碰撞
                if top <= -x:
                    stack.pop()
                # 当前负数小于或等于栈顶时，不再继续碰撞
                if -x <= top:
                    break
            else:
                stack.append(x)
        return stack


@pytest.mark.parametrize(('param', 'ret'), [
    ([5, 10, -5], [5, 10]),
    ([5, 10, 5], [5, 10, 5]),
    ([8, -8], []),
    ([-2, -1, 1, 2], [-2, -1, 1, 2]),
    ([-2, 1, -1, 2], [-2, 2]),
    ([10, 2, -5], [10])])
def test1(param, ret):
    solution = Solution()
    assert solution.asteroidCollision(param) == ret
