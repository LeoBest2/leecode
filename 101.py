#!/bin/python3
"""
    LeetCode 101.py
    ~~~~~
    @Description:
        给定一个二叉树，检查它是否是镜像对称的。

        例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

            1
           / \
          2   2
         / \ / \
        3  4 4  3
        但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

            1
           / \
          2   2
           \   \
           3    3
        说明:

        如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

    @CreateTime: 2019/12/14 15:03
    @Author: leo
    @License: MIT
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root: TreeNode) -> bool:
    if root is None:
        return True

    def _is_symmetric(l: TreeNode, r: TreeNode):
        if l is None or r is None:
            return l == r
        if l.val != r.val:
            return False
        return _is_symmetric(l.left, r.right) and _is_symmetric(l.right, r.left)
    return _is_symmetric(root.left, root.right)
