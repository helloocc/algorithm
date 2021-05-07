#!/usr/bin/env python
# -*- coding: utf8 -*-
import pytest


class Solution:

    def calculate(self, s: str) -> int:
        """使用栈

        1. 使用临时变量记录当前数字
        2. 遇到加减，则将当前数字直接入栈，减号入负数
        3. 遇到乘除，则将当前数字和栈顶数字进行运算再入栈
        """
        # 末尾补上+，以防最后一个数字不会加入stack
        s = s.replace(' ', '')+'+'
        stack = []
        num, op = 0, '+'
        for i, x in enumerate(s):
            if x.isdigit():
                num = num * 10 + int(x)
            else:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack[-1] *= num
                elif op == '/':
                    # 注意: -3//2=-2, 3//2=1
                    # 所以这里只能先/，再转化为int
                    stack.append(int(stack.pop() / num))
                num, op = 0, x
        return sum(stack)


@pytest.mark.parametrize(('param', 'ret'), [('3+2*2', 7),
                                            (' 3/2 ', 1),
                                            ('2*3+4/2', 8),
                                            ('14-3/2', 13),
                                            (' 3+5 / 2 ', 5)])
def test1(param, ret):
    solution = Solution()
    assert solution.calculate(param) == ret
