#!/usr/bin/env python
# -*- coding=utf8 -*-


from typing import List
import pytest


class Solution:
    def findDuplicate1(self, nums: List[int]) -> int:
        """
        一般意义上，我们都在索引维度上（空间），在给定target的情况下去二分查找。
        为什么能二分，是因为索引维度上数组有序。

        本题是在数值维度上去二分查找
        为什么能二分，是因为在数值维度上元素分布不均，存在二分条件（抽屉原理）。
        """
        n = len(nums) - 1
        # 这里不是索引维度，而是数值维度，所以left从1开始
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            # 以[1, 2, 2, 3, 4, 5, 6]为例
            # 小于等于3的数如果大于3，则重复元素一定在[1,3]区间内
            if count > mid:
                # 重复元素在[left,mid]区间
                right = mid
            else:
                # 否则在[mid+1,right]区间
                left = mid + 1

        return right

    def findDuplicate2(self, nums: List[int]) -> int:
        """
        快慢指针，比较难理解，参考142题解
        """
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        head = 0
        while head != slow:
            head = nums[head]
            slow = nums[slow]
        return head


@pytest.mark.parametrize(('param', 'ret'), [([1, 3, 4, 2, 2], 2),
                                            ([1, 2, 2, 3, 4, 5, 6], 2),
                                            ([1, 2, 3, 4, 5, 5], 5),
                                            ([1, 1, 2], 1),
                                            ([3, 1, 3, 4, 2], 3)])
def test1(param, ret):
    solution = Solution()
    assert solution.findDuplicate1(param) == ret
    assert solution.findDuplicate2(param) == ret
