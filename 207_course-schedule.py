#!/usr/bin/env python
# -*- coding=utf8 -*-
from typing import List
from collections import deque
import pytest


class Solution:
    """
    有向无环图，拓扑排序
    """

    def canFinish(self, numCourses: int,
                  prerequisites: List[List[int]]) -> bool:

        indegrees = [0] * numCourses
        adject = [[] for _ in range(numCourses)]
        queue = deque()

        # 获取入度和邻接表
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adject[pre].append(cur)

        for i, indgr in enumerate(indegrees):
            # 将入度为0的结点入队
            if not indgr:
                queue.append(i)

        while queue:
            # 弹出入度为0的结点
            pre = queue.popleft()
            numCourses -= 1

            for cur in adject[pre]:
                # 相应的结点入度-1
                indegrees[cur] -= 1
                # 入度为0进入队列
                if not indegrees[cur]:
                    queue.append(cur)

        return not numCourses


@pytest.mark.parametrize(('para1', 'para2', 'ret'),
                         [(2, [[1, 0]], True),
                          (2, [[1, 0], [0, 1]], False),
                          (3, [[2, 1], [1, 0]], True)])
def test1(para1, para2, ret):
    solution = Solution()
    assert solution.canFinish(para1, para2) == ret
