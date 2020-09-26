#!/usr/bin/env python
# -*- coding=utf8 -*-


class Solution:

    def generate(self, numRows: int) -> list:
        """
        使用一维数组
        """
        res = list()
        if numRows <= 0:
            return res

        res.append([1])
        if numRows == 1:
            return res

        for n in range(2, numRows+1):
            cur = [1]*n
            pre = res[n-2]
            for i in range(n-2):
                cur[i+1] = pre[i]+pre[i+1]
            res.append(cur)
        return res

    def generate2(self, numRows: int) -> list:
        """
        使用二维数组
        """
        ret = [[1 for y in range(x+1)] for x in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, len(ret[i])-1):
                ret[i][j] = ret[i-1][j-1]+ret[i-1][j]
        return ret


def test1():
    solution = Solution()
    assert solution.generate2(1) == [[1]]


def test2():
    solution = Solution()
    assert solution.generate(2) == [[1], [1, 1]]


def test3():
    solution = Solution()
    assert solution.generate(3) == [[1],
                                    [1, 1],
                                    [1, 2, 1]]


def test4():
    solution = Solution()
    assert solution.generate(4) == [[1],
                                    [1, 1],
                                    [1, 2, 1],
                                    [1, 3, 3, 1]]


def test5():
    solution = Solution()
    assert solution.generate2(5) == [[1],
                                     [1, 1],
                                     [1, 2, 1],
                                     [1, 3, 3, 1],
                                     [1, 4, 6, 4, 1]]
