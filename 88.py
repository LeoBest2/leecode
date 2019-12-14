#!/bin/python3
"""
    LeetCode 88.py
    ~~~~~
    @Description:
        给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

        说明:

        初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
        你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
        示例:

        输入:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3

        输出: [1,2,2,3,5,6]

    @CreateTime: 2019/12/14 13:01
    @Author: leo
    @License: MIT
"""


def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # a). 逆转nums1有数据的部分
    i, j = 0, m - 1
    while i < j:
        nums1[i], nums1[j] = nums1[j], nums1[i]
        i, j = i + 1, j - 1
    # b). 从后向前放最小的数
    i, j, cur_pos = m - 1, 0, m + n - 1
    while i >= 0 and j < n:
        if nums1[i] <= nums2[j]:
            nums1[cur_pos] = nums1[i]
            i -= 1
        else:
            nums1[cur_pos] = nums2[j]
            j += 1
        cur_pos -= 1
    while i >= 0:
        nums1[cur_pos] = nums1[i]
        i, cur_pos = i - 1, cur_pos - 1
    while j < n:
        nums1[cur_pos] = nums2[j]
        j, cur_pos = j + 1, cur_pos - 1
    nums1.reverse()
    return nums1


print(merge([1, 2, 7, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(merge([1, 2, 3, 4, 5], 5, [], 0))
print(merge([0, 0, 0, 0, 0], 0, [1, 2, 3, 4, 5], 5))
