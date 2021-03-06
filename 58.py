#!/bin/python3
"""
    LeetCode 58.py
    ~~~~~
    @Description:
        给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

        如果不存在最后一个单词，请返回 0 。

        说明：一个单词是指由字母组成，但不包含任何空格的字符串。

        示例:

        输入: "Hello World"
        输出: 5

    @CreateTime: 2019/12/14 10:10
    @Author: leo
    @License: MIT
"""


def lengthOfLastWord(s: str) -> int:
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    # 从最后便利找到第一个不为空的字符位置
    j = i
    while j >= 0 and s[j] != ' ':
        j -= 1
    return i - j


print(lengthOfLastWord("Hello World"))
