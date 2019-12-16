#!/bin/python3
"""
    LeetCode 110.py
    ~~~~~
    @Description:
        给定一个二叉树，判断它是否是高度平衡的二叉树。

        本题中，一棵高度平衡二叉树定义为：

        一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

        示例 1:

        给定二叉树 [3,9,20,null,null,15,7]

            3
           / \
          9  20
            /  \
           15   7
        返回 true 。

        示例 2:

        给定二叉树 [1,2,2,3,3,null,null,4,4]

               1
              / \
             2   2
            / \
           3   3
          / \
         4   4
        返回 false 。

    @CreateTime: 2019/12/16 13:51
    @Author: leo
    @License: MIT
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isBalanced(root: TreeNode) -> bool:
    if root is None:
        return True
    left_depth = _max_child_depths(root.left, 0)
    right_depth = _max_child_depths(root.right, 0)
    return (abs(left_depth-right_depth) < 2) and isBalanced(root.left) and isBalanced(root.right)


def _max_child_depths(node: TreeNode, depth: int):
    if node is None:
        return depth
    left_depth = _max_child_depths(node.left, depth+1)
    right_depth = _max_child_depths(node.right, depth+1)
    return max(left_depth, right_depth)


