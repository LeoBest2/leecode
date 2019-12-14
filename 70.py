#!/bin/python3
"""
    LeetCode 70.py
    ~~~~~
    @Description:
        假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

        每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

        注意：给定 n 是一个正整数。

        示例 1：

        输入： 2
        输出： 2
        解释： 有两种方法可以爬到楼顶。
        1.  1 阶 + 1 阶
        2.  2 阶
        示例 2：

        输入： 3
        输出： 3
        解释： 有三种方法可以爬到楼顶。
        1.  1 阶 + 1 阶 + 1 阶
        2.  1 阶 + 2 阶
        3.  2 阶 + 1 阶

    @CreateTime: 2019/12/14 11:30
    @Author: leo
    @License: MIT
"""


def climbStairs(n: int) -> int:
    """
    s(1) = 1
    s(2) = 2
    s(n) = s(n-1) + s(n-2)
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    x, y, i = 1, 2, 2
    while i < n:
        x, y = y, x + y
        i += 1
    return y


print(climbStairs(3))
print(climbStairs(4))
print(climbStairs(38))
