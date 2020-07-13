#!/usr/bin/env python
#-*- coding=utf8 -*-

from typing import List
import collections
import pytest

class Solution:
    """
    思路：
    1.假设AAABBCD，n=2。那么满足任务间隔要求，即：AXXAXXA，X表示需要填充任务或者idle的间隔
    2.如果有两种或两种以上的任务具有相同的最多的任务数，如：AAAABBBBCCDE，n=3。那么将相同个数
的任务A和B视为一个任务对，最终满足要求的分配为：ABXXABXXABXXAB，剩余的任务在不违背要求间隔的情况下穿插进间隔位置即可，空缺位置补idle
    3.由分析可以推导最少的任务时间：(最多任务数-1)*(n+1)+相同最多任务的任务个数。
      其中，(最多任务数-1)*(n+1) 计算ABXXABXXABXX，相同最多任务的任务个数 计算最后一个AB长度.
      具体计算即：(num(A)-1) * (3+1) + (2)
    4.最后，任务需要全部执行，所以取计算值和任务长度两者较大值（测试用例2场景）
    """

    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = collections.Counter(tasks)
        max_times = max(count.values())
        len_max = list(count.values()).count(max_times)
        return max(len(tasks), (max_times-1)*(n+1) + len_max)


@pytest.mark.parametrize(('param1', 'param2', 'res'), [
    (['A', 'A', 'A', 'B', 'B', 'B'], 2, 8),
    (['A', 'A', 'A', 'B', 'B', 'B'], 0, 6),
    (['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'], 2, 16)
])
def test1(param1, param2, res):
    s = Solution()
    assert s.leastInterval(param1, param2) == res
