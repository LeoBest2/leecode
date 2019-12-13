#!/bin/python3
"""
    LeetCode 28.py
    ~~~~~
    @Description:
        实现 strStr() 函数。

        给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

        示例 1:

        输入: haystack = "hello", needle = "ll"
        输出: 2
        示例 2:

        输入: haystack = "aaaaa", needle = "bba"
        输出: -1
        说明:

        当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

        对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。

    @CreateTime: 2019/12/13 9:54 下午
    @Author: leo
    @License: MIT
"""


def strStr(haystack: str, needle: str) -> int:
    if needle == '':
        return 0
    i = 0
    while i < len(haystack):
        # 判断长度，减少不必要的比较
        if len(haystack) - i < len(needle):
            return -1
        j = 0
        while j < len(needle):
            if haystack[i] != needle[j]:
                break
            i, j = i + 1, j + 1
        if j == len(needle):
            return i - j
        else:
            i = i - j + 1
    return -1


print(strStr("hello", "ll"))
print(strStr("hello", ""))
print(strStr("", ""))
print(strStr("aaaaa", "bba"))
print(strStr("aaa", "aaaa"))
