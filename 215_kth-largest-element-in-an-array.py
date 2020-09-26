#!/usr/bin/env python
# -*- coding=utf8 -*-
import pytest
from typing import List


class Solution:
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        """
        快排思想，分治，递归+partition
        每次快排都有一个数字达到最终位置，如果这个位置正好等于len(num)-k，则找到

        partition有两种，本方法是Hoare partition scheme
        """
        self.find = 0
        target = len(nums) - k

        def partition(low, high):
            if low > high:
                return
            lo, hi = low, high
            pivot = nums[lo]
            while lo < hi:
                while lo < hi and nums[hi] >= pivot:
                    hi -= 1
                nums[lo] = nums[hi]
                while lo < hi and nums[lo] < pivot:
                    lo += 1
                nums[hi] = nums[lo]
            nums[lo] = pivot
            return lo

        pos, left, right = -1, 0, len(nums) - 1
        while pos != target:
            pos = partition(left, right)
            if pos > target:
                right = pos - 1
            elif pos < target:
                left = pos + 1
        return nums[pos]

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        """
        另外一种partition: Lomuto partition scheme
        """
        self.find = 0
        target = len(nums) - k

        def partition(low, high):
            """
            遍历数组，i记录左边比pivot大的索引。
            遇到小于pivot的索引j时，交换ij。最后i的位置就是pivot的位置
            """
            if low > high:
                return
            pivot = nums[high]
            i = low
            for j in range(low, high):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[high] = nums[high], nums[i]
            return i

        pos, left, right = -1, 0, len(nums) - 1
        while pos != target:
            pos = partition(left, right)
            if pos > target:
                right = pos - 1
            elif pos < target:
                left = pos + 1
        return nums[pos]

    def findKthLargest4(self, nums: List[int], k: int) -> int:
        """
        TODO: 堆排序
        """


@pytest.mark.parametrize(('nums', 'target', 'ret'), [
    ([1], 1, 1),
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ([1, 2], 2, 1),
    ([1, 2], 1, 2),
    ([2, 1], 2, 1),
    ([1, 1], 1, 1)])
def test1(nums, target, ret):
    solution = Solution()
    assert solution.findKthLargest1(nums, target) == ret
    assert solution.findKthLargest2(nums, target) == ret
    assert solution.findKthLargest3(nums, target) == ret
