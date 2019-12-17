#!/bin/python3
"""
    LeetCode 118.py
    ~~~~~
    @Description:
        给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
        在杨辉三角中，每个数是它左上方和右上方的数的和。
        示例:
        输入: 5
        输出:
        [
             [1],
            [1,1],
           [1,2,1],
          [1,3,3,1],
         [1,4,6,4,1]
        ]

    @CreateTime: 2019/12/17 13:23
    @Author: leo
    @License: MIT
"""

from typing import List


def generate(numRows: int) -> List[List[int]]:
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    ret = [[1]]
    i = 2
    while i <= numRows:
        j, tmp = 1, [1]
        while j < i - 1:
            tmp.append(ret[i-2][j-1]+ret[i-2][j])
            j += 1
        tmp.append(1)
        ret.append(tmp)
        i += 1
    return ret


print(generate(8))
