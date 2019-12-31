#!/usr/bin/env python
# -*- coding=utf8 -*-


class Solution:
    def spiralOrder(self, matrix: list) -> list:
        """
        递归：每次遍历最外层，特殊处理只有一行或者一列的场景。
        """
        if not matrix:
            return []
        m, n = len(matrix)-1, len(matrix[0])-1
        res = []
        self.recursive(0, 0, m, n, matrix, res)
        return res

    def recursive(self, x_start, y_start, x_end, y_end, matrix, res):
        if x_start < x_end and y_start < y_end:
            for y in range(y_start, y_end):
                res.append(matrix[x_start][y])
            for x in range(x_start, x_end):
                res.append(matrix[x][y_end])
            for y in range(y_end, y_start, -1):
                res.append(matrix[x_end][y])
            for x in range(x_end, x_start, -1):
                res.append(matrix[x][y_start])
            x_start += 1
            x_end -= 1
            y_start += 1
            y_end -= 1
            self.recursive(x_start, y_start, x_end, y_end, matrix, res)
        elif x_start == x_end:
            res.extend([matrix[x_start][j] for j in range(y_start, y_end+1)])
        elif y_start == y_end:
            res.extend([matrix[i][y_end] for i in range(x_start, x_end+1)])

    def spiralOrder2(self, matrix: list) -> list:
        """
        直接对matrix进行pop操作。
        """
        res = []
        while matrix:
            res.extend(matrix.pop(0))  # left to right
            if matrix and matrix[0]:  # top to dwon
                for row in matrix:
                    res.append(row.pop())
            if matrix:  # right to left
                res.extend(matrix.pop()[::-1])
            if matrix and matrix[0]:  # bottom to up
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res


def test1():
    s = Solution()
    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    assert s.spiralOrder(a) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test2():
    s = Solution()
    a = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]
    assert s.spiralOrder(a) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


def test3():
    s = Solution()
    a = [[1, 2],
         [4, 5],
         [7, 8]]
    assert s.spiralOrder(a) == [1, 2, 5, 8, 7, 4]


def test4():
    s = Solution()
    a = [[1, 2],
         [7, 8]]
    assert s.spiralOrder(a) == [1, 2, 8, 7]


def test5():
    s = Solution()
    a = [[1, 2, 3]]
    assert s.spiralOrder(a) == [1, 2, 3]


def test6():
    s = Solution()
    a = [[2, 3, 4],
         [5, 6, 7],
         [8, 9, 10],
         [11, 12, 13],
         [14, 15, 16]]
    assert s.spiralOrder2(a) == [2, 3, 4, 7, 10, 13,
                                 16, 15, 14, 11, 8, 5, 6, 9, 12]
