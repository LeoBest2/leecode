#!/bin/python3
"""
    LeetCode 7.py
    ~~~~~
    @Description:

    @CreateTime: 2019/12/12 10:40 下午
    @Author: leo
    @License: MIT
"""


def reverse(x: int) -> int:
    if x > 0:
        positive = True
    elif x < 0:
        x = -x
        positive = False
    else:
        return 0
    m, n = x, 0
    while n == 0:
        n = m % 10
        m = (m-n) // 10
    ret = n
    while m > 0:
        n = m % 10
        m = (m-n) // 10
        ret = ret * 10 + n
    if ret > pow(2, 31) - 1:
        return 0
    if not positive:
        ret = -ret
    return ret


print(reverse(123))
print(reverse(-123))
print(reverse(120))
