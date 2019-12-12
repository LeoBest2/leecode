#!/bin/python3
"""
    LeetCode 20.py
    ~~~~~
    @Description:
        给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

        有效字符串需满足：

        左括号必须用相同类型的右括号闭合。
        左括号必须以正确的顺序闭合。
        注意空字符串可被认为是有效字符串。

        示例 1:

        输入: "()"
        输出: true
        示例 2:

        输入: "()[]{}"
        输出: true
        示例 3:

        输入: "(]"
        输出: false
        示例 4:

        输入: "([)]"
        输出: false
        示例 5:

        输入: "{[]}"
        输出: true

    @CreateTime: 2019/12/12 11:56 下午
    @Author: leo
    @License: MIT
"""


def isValid(s: str) -> bool:
    stack = []
    try:
        for char in s:
            if char in '([{':
                stack.append(char)
            elif char == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
            elif char == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()
            else:
                if stack[-1] != '{':
                    return False
                stack.pop()
    except IndexError:
        return False
    return len(stack) == 0


print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))
