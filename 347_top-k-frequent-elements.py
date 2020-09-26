#!/usr/bin/env python
# -*- coding=utf8 -*-

import pytest
from typing import List


class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums)
        return [x[0] for x in count.most_common(k)]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        """
        TODO: 堆排序
        """
        pass


@pytest.mark.parametrize(('nums', 'k', 'res'), [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
    ([1, 2, 2], 1, [2])])
def test1(nums, k, res):
    s = Solution()
    assert s.topKFrequent1(nums, k) == res
