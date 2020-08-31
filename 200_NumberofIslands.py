#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
import pytest


class Solution:
    """
    Flood fill算法是从一个区域中提取若干个连通的点与其他相邻区域区分开（或分别染成不同颜色）的经典算法
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # 方向数组，表示相对于当前位置的4个方向横纵坐标的偏移量，这是一个常见的技巧
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(i, j, grid, directions)
                    count += 1
        return count

    def dfs(self, i, j, grid, directions):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
            # 访问过的grid原地替换，也可以用额外数组visited进行标记
            grid[i][j] = '#'
            for direction in directions:
                # 分别访问四周的grid
                self.dfs(i + direction[0], j + direction[1], grid, directions)


@pytest.mark.parametrize(('param', 'ret'), [
    ([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]], 1),
    ([
        ["1", "1", "0"],
        ["1", "1", "0"],
        ["0", "0", "1"]], 2),
    ([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]], 3)])
def test1(param, ret):
    solution = Solution()
    assert solution.numIslands(param) == ret
