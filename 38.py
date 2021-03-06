#!/bin/python3
"""
    LeetCode 38.py
    ~~~~~
    @Description:
        报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：

        1.     1
        2.     11
        3.     21
        4.     1211
        5.     111221
        1 被读作  "one 1"  ("一个一") , 即 11。
        11 被读作 "two 1s" ("两个一"）, 即 21。
        21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

        给定一个正整数 n（1 ≤ n ≤ 30），输出报数序列的第 n 项。

        注意：整数顺序将表示为一个字符串。

         

        示例 1:

        输入: 1
        输出: "1"
        示例 2:

        输入: 4
        输出: "1211"

    @CreateTime: 2019/12/13 10:25 下午
    @Author: leo
    @License: MIT
"""


def countAndSay(n: int) -> str:
    if n == 1:
        return '1'
    i, ret = 1, '1'
    while i < n:
        j, tmp = 0, ''
        while j < len(ret):
            count = 0
            prev = ret[j]
            while j < len(ret) and ret[j] == prev:
                j, count = j + 1, count + 1
            tmp += '%d%s' % (count, ret[j-1])
        ret = tmp
        i += 1
    return ret


print(countAndSay(1))
print(countAndSay(2))
print(countAndSay(3))
print(countAndSay(4))
print(countAndSay(5))
print(countAndSay(10))
print(countAndSay(30))
