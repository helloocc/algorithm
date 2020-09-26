#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        从左上角开始查找，往下和右都是增大，从右下角查找，往左和上都是减小。没有意义
        因此，从左下角或右上角开始查找。
        对于左下角，往上是减小，往右是增大。
        对于右上角，往左是减小，往下是增大。
        """
        if not matrix:
            return False
        # 从左下角开始查找
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                i -= 1
            else:
                j += 1
        return False


@pytest.mark.parametrize(('nums', 'target', 'ret'), [
    ([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 5, True),
    ([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 20, False),
    (
        [], 1, False)])
def test1(nums, target, ret):
    solution = Solution()
    assert solution.searchMatrix(nums, target) == ret
