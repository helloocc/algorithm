#!/usr/bin/env python
# -*- coding=utf8 -*-


import pytest


class Solution:
    """
    荷兰国旗问题：https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    """

    def sortColors(self, nums: list) -> None:
        """
        假定三个区域和三个指针,l是小于区域的最右边，r是大于区域的最左边：

                  l    cur       r
                  |     |        |
        {小于区域} [未操作的数组] {大于区域}

        如果nums[cur]==0，则将cur指针与l交换，并向前移动l和cur指针。
        如果nums[cur]==1，则该元素已经在正确的位置，因此我们不必交换，只需将cur指针向前移动即可。
        如果nums[cur]==2，我们将交换最新的未分类元素。
        """

        l, cur, r = 0, 0, len(nums)-1
        while cur <= r:
            if nums[cur] < 1:
                nums[cur], nums[l] = nums[l], nums[cur]
                # cur需要移动因为交换后的cur是从l来的，l是我们默认的最后一个0的下一位，即1
                l += 1
                cur += 1
            elif nums[cur] > 1:
                nums[cur], nums[r] = nums[r], nums[cur]
                # 此时不需要移动cur，因为交换后的nums[cur]的值还不知道
                r -= 1
            else:
                # 即nums[cur]为1，默认放中间
                cur += 1
        return nums


@pytest.mark.parametrize(('param,ret'), [([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
                                         ([1, 0, 2], [0, 1, 2]),
                                         ([2, 0, 1], [0, 1, 2]),
                                         ([2, 1, 0], [0, 1, 2])])
def test(param, ret):
    s = Solution()
    assert s.sortColors(param) == ret
