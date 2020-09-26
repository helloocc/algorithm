#!/usr/bin/env python
# -*- coding=utf8 -*-


class Solution:
    def setZeroes1(self, matrix: list) -> None:
        if not matrix:
            return

        x_len, y_len = len(matrix), len(matrix[0])
        zero_set = set()
        for x in range(x_len):
            for y in range(y_len):
                if not matrix[x][y]:
                    zero_set.add((x, y))

        for x, y in zero_set:
            for i in range(x_len):
                matrix[i][y] = 0

            for j in range(y_len):
                matrix[x][j] = 0

        return matrix

    def setZeroes2(self, matrix: list) -> None:
        """
        记录0所在的行数和列数,统一修改
        """
        if not matrix:
            return
        x_len, y_len = len(matrix), len(matrix[0])
        x_set, y_set = set(), set()
        for x in range(x_len):
            for y in range(y_len):
                if not matrix[x][y]:
                    x_set.add(x)
                    y_set.add(y)

        # 可以直接修改一整行
        for x in x_set:
            matrix[x] = [0]*y_len

        for y in y_set:
            for x in range(x_len):
                matrix[x][y] = 0

        return matrix


def test1():
    s = Solution()
    a = [[1, 1, 1],
         [1, 0, 1],
         [1, 1, 1]]

    b = [[1, 0, 1],
         [0, 0, 0],
         [1, 0, 1]]
    assert s.setZeroes1(a) == b


def test2():
    s = Solution()
    a = [[0, 1, 2, 0],
         [3, 4, 5, 2],
         [1, 3, 1, 5]]

    b = [[0, 0, 0, 0],
         [0, 4, 5, 0],
         [0, 3, 1, 0]]
    assert s.setZeroes2(a) == b
