#!/bin/python3
"""
    LeetCode 121.py
    ~~~~~
    @Description:
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

        如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

        注意你不能在买入股票前卖出股票。

        示例 1:

        输入: [7,1,5,3,6,4]
        输出: 5
        解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
             注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
        示例 2:

        输入: [7,6,4,3,1]
        输出: 0
        解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

    @CreateTime: 2019/12/17 14:05
    @Author: leo
    @License: MIT
"""
import sys
from typing import List


def maxProfit(prices: List[int]) -> int:
    #
    # 计算出相邻两个节点间的差价, 在结果集中找到最大和的子序列
    #
    # i, diff = 0, []
    # while i < len(prices) - 1:
    #     diff.append(prices[i+1]-prices[i])
    #     i += 1
    #
    # def _find_max_sums(left: int, right: int) -> int:
    #     if left > right:
    #         return - sys.maxsize
    #     mid = (left+right+1) // 2
    #     mid_sum, m, n, max_mid_sum = diff[mid], mid-1, mid+1, diff[mid]
    #     while m >= left:
    #         mid_sum += diff[m]
    #         if mid_sum > max_mid_sum:
    #             max_mid_sum = mid_sum
    #         m -= 1
    #     mid_sum = max_mid_sum
    #     while n <= right:
    #         mid_sum += diff[n]
    #         if mid_sum > max_mid_sum:
    #             max_mid_sum = mid_sum
    #         n += 1
    #     return max(max_mid_sum, _find_max_sums(left, mid-1), _find_max_sums(mid+1, right))
    #
    # ret = _find_max_sums(0, len(diff)-1)
    # return 0 if ret < 0 else ret
    if len(prices) < 1:
        return 0
    min_price, max_profile = prices[0], 0
    i = 0
    while i < len(prices):
        min_price = min(min_price, prices[i])
        max_profile = max(max_profile, prices[i] - min_price)
        i += 1
    return max_profile


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
