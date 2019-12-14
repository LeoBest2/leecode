#!/bin/python3
"""
    LeetCode 67.py
    ~~~~~
    @Description:
        给定两个二进制字符串，返回他们的和（用二进制表示）。

        输入为非空字符串且只包含数字 1 和 0。

        示例 1:

        输入: a = "11", b = "1"
        输出: "100"
        示例 2:

        输入: a = "1010", b = "1011"
        输出: "10101"

    @CreateTime: 2019/12/14 10:32
    @Author: leo
    @License: MIT
"""


def addBinary(a: str, b: str) -> str:
    s, i, j = [], len(a) - 1, len(b) - 1
    flag = 0
    while i >= 0 and j >= 0:
        _sum = int(a[i]) + int(b[j]) + flag
        s.insert(0, str(_sum % 2))
        if _sum > 1:
            flag = 1
        else:
            flag = 0
        i, j = i - 1, j - 1
    if i > j:
        k, rest = i, a
    else:
        k, rest = j, b
    # print(k, rest, flag, s)
    while k >= 0:
        _sum = int(rest[k]) + flag
        s.insert(0, str(_sum % 2))
        if _sum > 1:
            flag = 1
        else:
            flag = 0
        k -= 1
    if flag == 1:
        s.insert(0, '1')
    return ''.join(s)


print(addBinary("101111", "10"))
print(addBinary("11", "1"))
print(addBinary("1010", "1011"))
print(addBinary("111", "110000"))
