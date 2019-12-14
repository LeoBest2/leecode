#!/bin/python3
"""
    LeetCode 69.py
    ~~~~~
    @Description:
        实现 int sqrt(int x) 函数。

        计算并返回 x 的平方根，其中 x 是非负整数。

        由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

        示例 1:

        输入: 4
        输出: 2
        示例 2:

        输入: 8
        输出: 2
        说明: 8 的平方根是 2.82842...,
             由于返回类型是整数，小数部分将被舍去。

    @CreateTime: 2019/12/14 11:06
    @Author: leo
    @License: MIT
"""


def mySqrt(x: int) -> int:
    a = 1
    for i in range(100):
        a = (a + x / a) / 2
    return int(a)


print(mySqrt(8))
