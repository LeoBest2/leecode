#!/bin/python3
"""
    LeetCode 122.py
    ~~~~~
    @Description:
        给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

        设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

        注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

        示例 1:

        输入: [7,1,5,3,6,4]
        输出: 7
        解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
             随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
        示例 2:

        输入: [1,2,3,4,5]
        输出: 4
        解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
             注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
             因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
        示例 3:

        输入: [7,6,4,3,1]
        输出: 0
        解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

    @CreateTime: 2019/12/19 16:10
    @Author: leo
    @License: MIT
"""

from typing import List


def maxProfit(prices: List[int]) -> int:
    def _max_profit_per(left: int, right: int) -> (int, int):
        if right - left < 1:
            return -1, -1
        # 找到第一个有比后面小的值
        i = left
        while i < right and prices[i] >= prices[i+1]:
            i += 1
        j = i + 1
        # 如果后面还有更大的值, 继续向后遍历
        while j < right and prices[j] <= prices[j+1]:
            j += 1
        if i == right:
            return -1, -1
        # print('当前找到的一个最小最大值位置为: [%s, %s], 值为 [%s, %s]' % (i, j, prices[i], prices[j]))
        return i, j
    first_min_pos, first_max_pos = _max_profit_per(0, len(prices)-1)
    s, max_profit = [], 0
    while first_min_pos != -1 and first_max_pos != -1:
        sec_min_pos, sec_max_pos = _max_profit_per(first_max_pos+1, len(prices)-1)
        if sec_min_pos == -1 or sec_max_pos == -1:
            max_profit += prices[first_max_pos] - prices[first_min_pos]
            break
        if prices[sec_min_pos] <= prices[first_max_pos]:
            max_profit += prices[first_max_pos] - prices[first_min_pos]
            first_min_pos, first_max_pos = sec_min_pos, sec_max_pos
        else:
            first_max_pos = sec_max_pos

    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([1, 2, 3, 4, 5]))
print(maxProfit([7, 6, 4, 3, 1]))
