#!/bin/python3
"""
    LeetCode 136.py
    ~~~~~
    @Description:
        给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

        说明：

        你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

        示例 1:

        输入: [2,2,1]
        输出: 1
        示例 2:

        输入: [4,1,2,1,2]
        输出: 4

    @CreateTime: 2019/12/19 7:49 下午
    @Author: leo
    @License: MIT
"""

from typing import List


def singleNumber(nums: List[int]) -> int:
    i, x = 1, nums[0]
    while i < len(nums):
        x ^= nums[i]
        i += 1
    return x


print(singleNumber([2, 2, 1]))
print(singleNumber([4, 1, 2, 1, 2]))
