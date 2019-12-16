#!/bin/python3
"""
    LeetCode 53.py
    ~~~~~
    @Description:
        给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

        示例:

        输入: [-2,1,-3,4,-1,2,1,-5,4],
        输出: 6
        解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
        进阶:

        如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

    @CreateTime: 2019/12/14 9:58
    @Author: leo
    @License: MIT
"""


def maxSubArray(nums: [int]) -> int:
    def _max_sub_array(left: int, right: int) -> int:
        if left == right:
            return nums[left]
        mid = (left + right + 1) // 2
        max_left, max_right = None, None
        if left <= mid - 1:
            max_left = _max_sub_array(left, mid - 1)
        if right >= mid + 1:
            max_right = _max_sub_array(mid + 1, right)
        # 从中间位置向左遍历到最大和
        i, _sum, max_mid = mid - 1, nums[mid], nums[mid]
        while i >= left:
            _sum += nums[i]
            if _sum >= max_mid:
                max_mid = _sum
            i -= 1
        # 再从中间位置向右遍历
        j, _sum = mid + 1, max_mid
        while j <= right:
            _sum += nums[j]
            if _sum >= max_mid:
                max_mid = _sum
            j += 1
        return max(max_mid, max_mid if max_left is None else max_left, max_mid if max_right is None else max_right)

    return _max_sub_array(0, len(nums) - 1)


print(maxSubArray([-1, -2, -3, 0]))
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSubArray([-2, -1]))
print(maxSubArray([-2, -1, 3, -4, 5]))
