#!/bin/python3
"""
    LeetCode 119.py
    ~~~~~
    @Description:
        给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

        在杨辉三角中，每个数是它左上方和右上方的数的和。

        示例:

        输入: 3
        输出: [1,3,3,1]

    @CreateTime: 2019/12/17 13:43
    @Author: leo
    @License: MIT
"""

from typing import List


def getRow(rowIndex: int) -> List[int]:
    """
    [1, Ck2, Ck3, ...Ckk, 1]
    """

    def _sort_count(n, k):
        _n_sum, _k_sum = 1, 1
        i = k
        while i > 0:
            _n_sum *= n
            i, n = i - 1, n - 1
        while k > 1:
            _k_sum *= k
            k -= 1
        return _n_sum // _k_sum
    ret = []
    for j in range(rowIndex+1):
        ret.append(_sort_count(rowIndex, j))
    return ret


print(getRow(4))
print(getRow(5))
print(getRow(6))
print(getRow(7))
print(getRow(33))
