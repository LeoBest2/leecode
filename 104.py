#!/bin/python3
"""
    LeetCode 104.py
    ~~~~~
    @Description:
        给定一个二叉树，找出其最大深度。

        二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

        说明: 叶子节点是指没有子节点的节点。

        示例：
        给定二叉树 [3,9,20,null,null,15,7]，

            3
           / \
          9  20
            /  \
           15   7
        返回它的最大深度 3 。

    @CreateTime: 2019/12/14 15:05
    @Author: leo
    @License: MIT
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root: TreeNode) -> int:
    def _max_depth(node: TreeNode, max_depth: int) -> int:
        if node is None:
            return max_depth
        max_depth += 1
        left_max_depth = _max_depth(node.left, max_depth)
        right_max_depth = _max_depth(node.right, max_depth)
        if left_max_depth > right_max_depth:
            return left_max_depth
        else:
            return right_max_depth
    return _max_depth(root, 0)
