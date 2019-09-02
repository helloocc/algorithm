#!/usr/bin/env python
# -*- coding=utf8 -*-


class Solution:
    def insertSort(self, l: list) -> list:
        """
        分为已排序区间和未排序区间。
        取未排序区间中的元素，在已排序区间中找到合适的位置插入，并保证已排序区间一直有序。

        场景：类似打扑克时摸牌，新摸一张时插入手里已经排好序的牌中。
        """
        for i in range(1, len(l)):
            key = l[i]
            j = i-1
            while j >= 0 and l[j] > key:
                l[j+1] = l[j]
                j -= 1
            l[j+1] = key

        return l

    def bubbleSort(self, l: list) -> list:
        """
        冒泡排序比较相邻元素，每次都至少有一个元素移到最终位置。
        如果一次比较没有发生数据交换，则已经有序。
        """
        for i in range(len(l))[::-1]:
            change = False
            for j in range(0, i):
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]
                    change = True
            if not change:
                break
        return l

    def quickSort(self, data: list, low: int, high: int) -> list:
        """
        取一个pivot，小于pivot的放左边，大于pivot的放右边，pivot放到中间。
        分治递归思想，递归快排pivot左边的和右边的数字。
        """
        if low >= high:
            return data
        l = low
        h = high
        pivot = data[l]
        while l < h:
            while l < h and pivot <= data[h]:
                h -= 1
            data[l] = data[h]
            while l < h and pivot >= data[l]:
                l += 1
            data[h] = data[l]
        data[l] = pivot
        self.quickSort(data, low, l-1)
        self.quickSort(data, l+1, high)
        return data


class Test:
    import pytest

    @pytest.mark.parametrize('nums,ret', [
        ([1, 5, 2, 3, 6, 4], [1, 2, 3, 4, 5, 6]),
        ([1, 5, 2, 3, 6, 4, 5], [1, 2, 3, 4, 5, 5, 6]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([38, 29, 12, 8], [8, 12, 29, 38]),
        ([38, 29, 12, 8, 1], [1, 8, 12, 29, 38]),
        ([5, 2], [2, 5]),
        ([1], [1]),
        ([], []),
    ])
    def test_Sort(self, nums, ret):
        s = Solution()

        a = list(nums)
        assert s.quickSort(a, 0, len(a)-1) == ret

        # 重新new对象，否则直接传nums是上面已经排序好的
        b = list(nums)
        assert s.bubbleSort(b) == ret

        c = list(nums)
        assert s.insertSort(c) == ret
