#!/usr/bin/env python
# -*- coding=utf8 -*-


class Solution:
    """
    https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)
    """

    def rotate1(self, matrix: list) -> None:
        """
        zip解压后是tuple，需要转为list
        """
        matrix[:] = map(list, zip(*matrix[::-1]))
        return matrix

    def rotate2(self, matrix: list) -> None:
        """
        先reverse，再沿着对角线翻转
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix


def test1():
    s = Solution()
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    natrix = [[7, 4, 1],
              [8, 5, 2],
              [9, 6, 3]]
    assert s.rotate1(matrix) == natrix


def test2():
    s = Solution()
    matrix = [[5, 1, 9, 11],
              [2, 4, 8, 10],
              [13, 3, 6, 7],
              [15, 14, 12, 16]
              ]

    natrix = [[15, 13, 2, 5],
              [14, 3, 4, 1],
              [12, 6, 8, 9],
              [16, 7, 10, 11]
              ]
    assert s.rotate2(matrix) == natrix
