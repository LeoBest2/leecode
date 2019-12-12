#!/bin/python3
"""
    LeetCode 14.py
    ~~~~~
    @Description:
        编写一个函数来查找字符串数组中的最长公共前缀。

        如果不存在公共前缀，返回空字符串 ""。

        示例 1:

        输入: ["flower","flow","flight"]
        输出: "fl"
        示例 2:

        输入: ["dog","racecar","car"]
        输出: ""
        解释: 输入不存在公共前缀。
        说明:

        所有输入只包含小写字母 a-z 。
    @CreateTime: 2019/12/12 11:30 下午
    @Author: leo
    @License: MIT
"""


def longestCommonPrefix(strs) -> str:
    if len(strs) == 0:
        return ''
    if len(strs) == 1:
        return strs[0]
    i = 0
    try:
        while True:
            s = strs[0][i]
            for _ in strs:
                if s != _[i]:
                    return strs[0][:i]
            i += 1
    except IndexError:
        return strs[0][:i]


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
