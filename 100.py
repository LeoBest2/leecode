#!/bin/python3
"""
    LeetCode 100.py
    ~~~~~
    @Description:
        给定两个二叉树，编写一个函数来检验它们是否相同。

        如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

        示例 1:

        输入:       1         1
                  / \       / \
                 2   3     2   3

                [1,2,3],   [1,2,3]

        输出: true
        示例 2:

        输入:      1          1
                  /           \
                 2             2

                [1,2],     [1,null,2]

        输出: false
        示例 3:

        输入:       1         1
                  / \       / \
                 2   1     1   2

                [1,2,1],   [1,1,2]

        输出: false

    @CreateTime: 2019/12/14 14:45
    @Author: leo
    @License: MIT
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if p is None or q is None:
        return p == q
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
