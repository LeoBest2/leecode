#!/bin/python3
"""
    LeetCode 112.py
    ~~~~~
    @Description:
        给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

        说明: 叶子节点是指没有子节点的节点。

        示例: 
        给定如下二叉树，以及目标和 sum = 22，

                      5
                     / \
                    4   8
                   /   / \
                  11  13  4
                 /  \      \
                7    2      1
        返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。

    @CreateTime: 2019/12/16 16:33
    @Author: leo
    @License: MIT
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root: TreeNode, _sum: int) -> bool:
    def _mid_parse_tree(node: TreeNode, __sum: int) -> bool:
        if node is None:
            return False
        __sum += node.val
        if node.left is None and node.right is None:
            return __sum == _sum
        return _mid_parse_tree(node.left, __sum) or _mid_parse_tree(node.right, __sum)

    return _mid_parse_tree(root, 0)
