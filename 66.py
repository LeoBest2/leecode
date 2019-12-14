#!/bin/python3
"""
    LeetCode 66.py
    ~~~~~
    @Description:
        给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

        最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

        你可以假设除了整数 0 之外，这个整数不会以零开头。

        示例 1:

        输入: [1,2,3]
        输出: [1,2,4]
        解释: 输入数组表示数字 123。
        示例 2:

        输入: [4,3,2,1]
        输出: [4,3,2,2]
        解释: 输入数组表示数字 4321。

    @CreateTime: 2019/12/14 10:17
    @Author: leo
    @License: MIT
"""


def plusOne(digits: [int]) -> [int]:
    i = len(digits) - 1
    _sum = digits[i] + 1
    while _sum >= 10:
        digits[i] = _sum % 10
        i -= 1
        if i < 0:
            digits.insert(0, 1)
            return digits
        _sum = digits[i] + 1
    digits[i] = _sum
    return digits


print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([4, 3, 9, 9]))
print(plusOne([9, 9, 9, 9]))
