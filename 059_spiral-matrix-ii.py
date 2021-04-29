#!/usr/bin/env python
# -*- coding: utf8 -*-
from typing import List
import pytest


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        # 用元祖表示四个方向
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        # 从1开始填充，填充n*n个数字
        num, target = 1, n * n
        # 起始点为(0,-1)，即第一个点(0,0)就是循环填充的结果
        i, j = 0, -1

        while num <= target:
            for direction in directions:
                x, y = direction
                # 下一步方向满足要求时，进行填充
                while (0 <= i+x < n and 0 <= j+y < n
                        and matrix[i+x][j+y] == 0):
                    matrix[i+x][j+y] = num
                    i += x
                    j += y
                    num += 1
        return matrix


@pytest.mark.parametrize(('param', 'ret'), [
    (1, [[1]]),
    (2, [[1, 2], [4, 3]]),
    (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]])])
def test1(param, ret):
    solution = Solution()
    assert solution.generateMatrix(param) == ret
