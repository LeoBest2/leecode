#!/bin/python3
"""
    LeetCode 107.py
    ~~~~~
    @Description:
        给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

        例如：
        给定二叉树 [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        返回其自底向上的层次遍历为：

        [
          [15,7],
          [9,20],
          [3]
        ]

    @CreateTime: 2019/12/14 15:12
    @Author: leo
    @License: MIT
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def levelOrderBottom(root: TreeNode) -> [[int]]:
    ret: [[int]] = []

    def _level_order_bottom(node: TreeNode, depth: int) -> None:
        if node is None:
            return
        if depth >= len(ret):
            ret.append([])
        _level_order_bottom(node.left, depth + 1)
        _level_order_bottom(node.right, depth + 1)
        ret[depth].append(node.val)

    _level_order_bottom(root, 0)
    ret.reverse()
    return ret
