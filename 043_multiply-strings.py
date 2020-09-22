#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest


class Solution:
    """
    主要思路就是模仿乘法，将高级的算法不断地转化为低级的过程，由两个字符串相乘->一个字符串与一个字符相乘->一个字符与一个字符相乘，然后找出相乘的结果在结果字符串中添加的位置

    参考：https://leetcode-cn.com/problems/multiply-strings/solution/gao-pin-mian-shi-xi-lie-zi-fu-chuan-cheng-fa-by-la/
    """

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        # 把num1和num2里外遍历的顺序反过来，按照常规的乘法顺序更容易理解
        for i in range(n)[::-1]:
            for j in range(m)[::-1]:
                multi = int(num2[i]) * int(num1[j])
                # 每两个数字的乘积的位置位于res[i+j,i+j+1]
                p1, p2 = i + j, i + j + 1
                div, mod = divmod(res[p2] + multi, 10)
                res[p2] = mod
                # 这里注意，res[p1]的数值可能大于10，但本次无需处理，下个循坏会处理进位
                res[p1] += div
        return ''.join(map(str, res)).lstrip('0')


@pytest.mark.parametrize(('num1', 'num2', 'ret'), [('2', '3', '6'),
                                                   ('123', '456', '56088'),
                                                   ('0', '0', '0'),
                                                   ('11', '11', '121')])
def test1(num1, num2, ret):
    solution = Solution()
    assert solution.multiply(num1, num2) == ret
