#!/bin/python3
"""
    LeetCode 9.py
    ~~~~~
    @Description:
        判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

        示例 1:

        输入: 121
        输出: true
        示例 2:

        输入: -121
        输出: false
        解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
        示例 3:

        输入: 10
        输出: false
        解释: 从右向左读, 为 01 。因此它不是一个回文数。
    @CreateTime: 2019/12/12 10:52 下午
    @Author: leo
    @License: MIT
"""


def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True
    m, n = x, 0
    n = m % 10
    m = (x-n) // 10
    if n == 0:
        return False
    ret = n
    while m > 0:
        n = m % 10
        m = (m-n) // 10
        ret = ret * 10 + n
    return ret == x


print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))
