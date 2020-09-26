#!/usr/bin/env python
#-*- coding=utf8 -*-

from typing import List
import pytest


class Solution:
    """
    思想：从i开始，要在后续数组中找到第一个比自己大的数值，并计算二者索引的差值，如果没有找到，就是0
    
    1. 使用单调递减栈，栈中元素都没有遇到第一个比自己大的数值，处于等待状态
    2. 当遇到一个值大于栈顶元素时，说明栈顶元素已经找到了目标值，记录索引差值并弹出栈顶
    3. 重复以上过程
    4. 最后，还留在栈中的元素，说明都没有找到目标值，全部标记为0即可
    """

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0]*len(T)
        stack = list()
        for i, x in enumerate(T):
            while stack and T[stack[-1]] < x:
                # 得到的是栈顶元素的结果
                res[stack[-1]] = i-stack[-1]
                stack.pop()
            else:
                # 栈中保存的是index而非value
                stack.append(i)
        return res


@pytest.mark.parametrize(('nums', 'res'), [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([1, 2, 3], [1, 1, 0]),
    ([3, 2, 1], [0, 0, 0]),
    ([1, 2, 5, 4, 3], [1, 1, 0, 0, 0])
])
def test1(nums, res):
    s = Solution()
    assert s.dailyTemperatures(nums) == res
