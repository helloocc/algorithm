#!/usr/bin/env python
# -*- coding=utf8 -*-


from typing import List
import pytest


class Solution:
    """
    DFS：以每个元素为起点，分别判断上下左右四个字符是否符合条件。符合条件则一直向下寻找，否则回退。
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if not word:
            return True
        if 0 <= i < len(board) and 0 <= j < len(board[0]) and word[0] == board[i][j]:
            # 已经使用过的元素需要替换，避免再次使用，例如用例ABCB
            board[i][j] = -1
            res = self.dfs(board, i - 1, j, word[1:]) or \
                self.dfs(board, i + 1, j, word[1:]) or \
                self.dfs(board, i, j - 1, word[1:]) or \
                self.dfs(board, i, j + 1, word[1:])
            # 重新替换回来，不影响下次访问
            board[i][j] = word[0]
            return res
        else:
            return False


@pytest.mark.parametrize(('word', 'res'), [('ABCCED', True),
                                           ('SEE', True),
                                           ('ABCB', False)])
def test1(word, res):
    board = [['A', 'B', 'C', 'E'],
             ['S', 'F', 'C', 'S'],
             ['A', 'D', 'E', 'E']]
    sol = Solution()
    assert sol.exist(board, word) == res
