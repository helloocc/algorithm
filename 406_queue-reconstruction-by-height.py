#!/usr/bin/env python
# -*- coding=utf8 -*-

from typing import List
import pytest


class Solution:
    """
    主要理解，为什么按身高降序按k升序排序，然后依次插入对应的k位置？

    1.矮的人相对于高的人是看不见的：因为k的值是前面比自己高或等高的人的个数，先处理高的人，满
足k的条件后，再处理矮的人不会破坏这个条件。

    2.同等高度的人插入对应的k位置：因为插入后要占据一个位置，所以之后同等高度的人只能在后面插
入，因此需要按k升序

    排序前：
    [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    排序后：
    [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]

    插入：
    [[7,0]]   (insert [7,0] at index 0)
    [[7,0],[7,1]]   (insert [7,1] at index 1)
    [[7,0],[6,1],[7,1]]   (insert [6,1] at index 1)
    [[5,0],[7,0],[6,1],[7,1]]   (insert [5,0] at index 0)
    [[5,0],[7,0],[5,2],[6,1],[7,1]]   (insert [5,2] at index 2)
    [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]   (insert [4,4] at index 4)
    """

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


@pytest.mark.parametrize(('nums', 'res'), [
    (
        [[7, 0], [5, 0], [5, 2]],
        [[5, 0], [7, 0], [5, 2]]
    ),
    (
        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
        [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    )
])
def test1(nums, res):
    s = Solution()
    assert s.reconstructQueue(nums) == res
