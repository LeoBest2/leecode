#!/bin/python3
"""
    LeetCode 155.py
    ~~~~~
    @Description:
        设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

        push(x) -- 将元素 x 推入栈中。
        pop() -- 删除栈顶的元素。
        top() -- 获取栈顶元素。
        getMin() -- 检索栈中的最小元素。
        示例:

        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin();   --> 返回 -3.
        minStack.pop();
        minStack.top();      --> 返回 0.
        minStack.getMin();   --> 返回 -2.

    @CreateTime: 2019/12/23 20:17
    @Author: leo
    @License: MIT
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.helper) == 0 or self.helper[-1] > x:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:
        self.data.pop()
        self.helper.pop()

    def top(self) -> int or None:
        return len(self.data) == 0 or self.data[-1]

    def getMin(self) -> int or None:
        return len(self.helper) == 0 or self.helper[-1]


min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-1)
print(min_stack.getMin())
print(min_stack.top())
print(min_stack.top())
print(min_stack.getMin())
