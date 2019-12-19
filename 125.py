#!/bin/python3
"""
    LeetCode 125.py
    ~~~~~
    @Description:
        给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

        说明：本题中，我们将空字符串定义为有效的回文串。

        示例 1:

        输入: "A man, a plan, a canal: Panama"
        输出: true
        示例 2:

        输入: "race a car"
        输出: false

    @CreateTime: 2019/12/19 7:28 下午
    @Author: leo
    @License: MIT
"""


def isPalindrome(s: str) -> bool:
    if s == '':
        return True
    i, j = 0, len(s)-1
    while i <= j:
        while i <= j - 1 and s[i] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            i += 1
        while i <= j - 1 and s[j] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            j -= 1
        if s[i].upper() != s[j].upper():
            return False
        i, j = i+1, j-1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))


