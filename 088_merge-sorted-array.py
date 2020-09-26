#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    def merge1(self, nums1: list, m: int, nums2: list, n: int) -> None:
        nums1[m:] = nums2
        nums1.sort()
        return nums1

    def merge2(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        逆序比较两个数组，每次都有一个数到达最终位置。
        当比较完nums2还有剩余时，自动补充到num1的前面。
        """
        m, n = m-1, n-1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[m+n+1] = nums1[m]
                m -= 1
            else:
                nums1[m+n+1] = nums2[n]
                n -= 1
        if n >= 0:
            nums1[:n+1] = nums2[:n+1]
        return nums1


@pytest.mark.parametrize(('nums1', 'm', 'nums2', 'n', 'ret'),
                         [([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
                          ([1, 2, 3, 0], 3, [5], 1, [1, 2, 3, 5]),
                          ([3, 5, 0, 0, 0], 2, [1, 2, 4], 3, [1, 2, 3, 4, 5]),
                          ([0], 0, [1], 1, [1]),
                          ([3, 0, 0], 1, [1, 2], 2, [1, 2, 3])])
def test1(nums1, m, nums2, n, ret):
    s = Solution()
    assert s.merge1(nums1, m, nums2, n) == ret


@pytest.mark.parametrize(('nums1', 'm', 'nums2', 'n', 'ret'),
                         [([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
                          ([1, 2, 3, 0], 3, [5], 1, [1, 2, 3, 5]),
                          ([3, 5, 0, 0, 0], 2, [1, 2, 4], 3, [1, 2, 3, 4, 5]),
                          ([0], 0, [1], 1, [1]),
                          ([3, 0, 0], 1, [1, 2], 2, [1, 2, 3])])
def test2(nums1, m, nums2, n, ret):
    s = Solution()
    assert s.merge2(nums1, m, nums2, n) == ret
