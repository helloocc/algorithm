#!/usr/bin/env python
# -*- coding: utf8 -*-


class MinStack:
    """关键点在于getMin只能是O(1)，pop后最小值可能会变需要重新遍历

    借用辅助栈(或单栈存数组)，同时记录val和当前的最小值
    """

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        cur_min = min(self.getMin(), val) if self.stack else val
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


def test1():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.getMin() == -2
