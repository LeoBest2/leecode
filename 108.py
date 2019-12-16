#!/bin/python3
"""
    LeetCode 108.py
    ~~~~~
    @Description:
        将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

        本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

        示例:

        给定有序数组: [-10,-3,0,5,9],

        一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

              0
             / \
           -3   9
           /   /
         -10  5

    @CreateTime: 2019/12/14 15:59
    @Author: leo
    @License: MIT
"""


from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(nums: [int]) -> TreeNode:

    def _sorted_array_to_bst(left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None
        mid = (left+right+1) // 2
        node = TreeNode(nums[mid])
        node.left = _sorted_array_to_bst(left, mid-1)
        node.right = _sorted_array_to_bst(mid+1, right)
        return node

    return _sorted_array_to_bst(0, len(nums)-1)


root = sortedArrayToBST([-10, -3, 0, 5, 9])
