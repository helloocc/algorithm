#!/usr/bin/env python
# -*- coding: utf8 -*-
from typing import List
import pytest


class Solution:
    """
    遍历每个城市，如果该城市未被访问过，即为一个新的区域，并用DFS/BFS访问相邻的城市
    """

    def findCircleNum1(self, isConnected: List[List[int]]) -> int:
        # DFS
        count = 0
        visited = [False] * len(isConnected)

        def dfs(i):
            visited[i] = True
            for j in range(len(isConnected)):
                if not visited[j] and isConnected[i][j]:
                    visited[j] = True
                    dfs(j)

        for i in range(len(isConnected)):
            if not visited[i]:
                count += 1
                dfs(i)
        return count

    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        # BFS
        count = 0
        queue = []
        visited = [False] * len(isConnected)

        for i in range(len(isConnected)):
            if not visited[i]:
                visited[i] = True
                count += 1
                queue.append(i)

                while queue:
                    k = queue.pop()
                    for j in range(len(isConnected)):
                        if not visited[j] and isConnected[k][j]:
                            visited[j] = True
                            queue.append(j)
        return count

    def findCircleNum3(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind()
        for i in range(len(isConnected)):
            uf.add(i)
            for j in range(i):
                if isConnected[i][j]:
                    uf.merge(i, j)

        return uf.num_of_sets


class UnionFind:
    """并查集
    https://leetcode-cn.com/problems/number-of-provinces/solution/python-duo-tu-xiang-jie-bing-cha-ji-by-m-vjdr/
    """

    def __init__(self):
        self.father = {}
        # 额外记录集合的数量
        self.num_of_sets = 0

    def find(self, x):
        root = x

        while self.father[root] is not None:
            root = self.father[root]

        # 路径压缩
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father

        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            # 集合的数量-1
            self.num_of_sets -= 1

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            # 集合的数量+1
            self.num_of_sets += 1


@pytest.mark.parametrize(('param', 'ret'), [
    ([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]], 1),
    ([
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]], 2),
    ([
        [1, 0, 1],
        [0, 1, 0],
        [1, 0, 1]], 2),
    ([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]], 3),
    ([
        [1, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 1, 1]], 1
     )])
def test1(param, ret):
    solution = Solution()
    assert solution.findCircleNum1(param) == ret
    assert solution.findCircleNum2(param) == ret
    assert solution.findCircleNum3(param) == ret
